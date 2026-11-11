import asyncio
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai import types
import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.rollen import (  # noqa: E402
    AGENTEN_ROLLEN,
    BERICHTS_ANWEISUNG,
    GESCHAEFTS_AGENTEN,
    STANDARD_AUFTRAG,
    AgentenBefund,
    AgentenRolle,
)

MODEL = os.environ.get("GEMINI_MODELL", "gemini-3.8-flash")
MIT_SUCHE = os.environ.get("NETZWERK_MIT_SUCHE", "0") == "1"
BACKEND = os.environ.get("NETZWERK_BACKEND", "gemini")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODELL = os.environ.get("OLLAMA_MODELL", "llama3.1:8b")
MAX_PARALLEL = int(os.environ.get("NETZWERK_MAX_PARALLEL", "3"))

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
AUSGABEN_DIR = REPO_ROOT / "ausgaben"

_drossel = asyncio.Semaphore(MAX_PARALLEL)


def _tools() -> list | None:
    if BACKEND != "gemini" or not MIT_SUCHE:
        return None
    return [types.Tool(google_search=types.GoogleSearch())]


def _system_anweisung(rolle: AgentenRolle) -> str:
    system = rolle.auftrag
    if BACKEND == "gemini" and not MIT_SUCHE:
        system = (
            "Hinweis: Du hast keinen Internetzugang. Arbeite mit deinem eigenen Wissen und "
            "kennzeichne veraltete oder unsichere Angaben als offen. " + system
        )
    if BACKEND == "ollama":
        system = (
            "Hinweis: Du laeuft lokal ohne Internetzugang. Arbeite mit deinem eigenen Wissen "
            "und kennzeichne unsichere Angaben als offen. " + system
        )
    return system


async def _ollama_chat(system: str, nutzer: str) -> str:
    async with httpx.AsyncClient(timeout=600) as client:
        antwort = await client.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": OLLAMA_MODELL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": nutzer},
                ],
                "stream": False,
            },
        )
        antwort.raise_for_status()
        return antwort.json()["message"]["content"].strip()


async def _gemini_chat(system: str, nutzer: str) -> str:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    antwort = await client.aio.models.generate_content(
        model=MODEL,
        contents=nutzer,
        config=types.GenerateContentConfig(system_instruction=system, tools=_tools()),
    )
    return (antwort.text or "").strip()


async def frage_agent(rolle: AgentenRolle, nutzer: str) -> str:
    system = _system_anweisung(rolle)
    if BACKEND == "ollama":
        async with _drossel:
            return await _ollama_chat(system, nutzer)
    async with _drossel:
        return await _gemini_chat(system, nutzer)


async def agent_recherche(client_placeholder, rolle: AgentenRolle, auftrag: str) -> AgentenBefund:
    text = (await frage_agent(rolle, auftrag)).strip()
    if not text:
        raise RuntimeError(f"Agent {rolle.name} hat keinen Befund geliefert.")
    return AgentenBefund(agent=rolle.name, befund=text)


async def bericht_konsolidieren(client_placeholder, auftrag: str, befunde: list[AgentenBefund]) -> str:
    berichts_rolle = AgentenRolle(
        name="bericht-agent", beschreibung="Konsolidiert Befunde", auftrag=BERICHTS_ANWEISUNG
    )
    befunde_text = "\n\n".join(f"### Befund von {befund.agent}\n{befund.befund}" for befund in befunde)
    bericht = await frage_agent(
        berichts_rolle, f"Auftrag: {auftrag}\n\nBefunde der Agenten:\n\n{befunde_text}"
    )
    if not bericht:
        raise RuntimeError("Berichts-Agent hat keinen Report geliefert.")
    return bericht


def report_text(auftrag: str, zeitstempel: datetime, bericht: str, befunde: list[AgentenBefund]) -> str:
    kopf = (
        f"# Jarvis Netzwerk-Bericht ({zeitstempel.strftime('%Y-%m-%d %H:%M UTC')})\n\n"
        f"**Backend:** {BACKEND} | **Auftrag:** {auftrag}\n\n"
        f"**Agenten:** {', '.join(befund.agent for befund in befunde)}\n\n"
        f"## Einzelbefunde\n\n"
    )
    befunde_markdown = "\n\n".join(f"### {befund.agent}\n\n{befund.befund}" for befund in befunde)
    return f"{kopf}{befunde_markdown}\n\n---\n\n{bericht}\n"


async def produziere_arbeitsproben(zeitstempel: datetime) -> list[tuple[str, Path]]:
    ablage = AUSGABEN_DIR / zeitstempel.strftime("%Y-%m-%d")
    ablage.mkdir(parents=True, exist_ok=True)

    async def eine(rolle: AgentenRolle) -> tuple[str, Path]:
        text = (await frage_agent(rolle, "Erstelle die heuteige Arbeitsprobe nach deiner Anweisung.")).strip()
        if not text:
            raise RuntimeError(f"Agent {rolle.name} hat keine Arbeitsprobe geliefert.")
        pfad = ablage / f"{rolle.name}.md"
        pfad.write_text(f"# Arbeitsprobe: {rolle.name}\n\n{text}\n", encoding="utf-8")
        return rolle.name, pfad

    return list(await asyncio.gather(*(eine(rolle) for rolle in GESCHAEFTS_AGENTEN)))


async def main() -> None:
    if BACKEND == "gemini" and not os.environ.get("GEMINI_API_KEY"):
        raise SystemExit("GEMINI_API_KEY ist nicht gesetzt (oder NETZWERK_BACKEND=ollama nutzen).")

    auftrag = " ".join(sys.argv[1:]) or STANDARD_AUFTRAG
    zeitstempel = datetime.now(timezone.utc)

    print(f"Backend: {BACKEND} | {len(AGENTEN_ROLLEN)} Recherche- + {len(GESCHAEFTS_AGENTEN)} Geschaefts-Agenten")

    proben = await produziere_arbeitsproben(zeitstempel)
    for name, pfad in proben:
        print(f"  Arbeitsprobe {name}: {pfad}")

    print(f"Starte {len(AGENTEN_ROLLEN)} Recherche-Agenten parallel ...")
    befunde = list(
        await asyncio.gather(*(agent_recherche(None, rolle, auftrag) for rolle in AGENTEN_ROLLEN))
    )
    for befund in befunde:
        print(f"  OK {befund.agent}: {len(befund.befund)} Zeichen")

    print("Konsolidiere Bericht ...")
    bericht = await bericht_konsolidieren(None, auftrag, befunde)

    pfad = REPORTS_DIR / f"{zeitstempel.strftime('%Y-%m-%d')}-netzwerk-bericht.md"
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(report_text(auftrag, zeitstempel, bericht, befunde), encoding="utf-8")
    print(f"Bericht gespeichert: {pfad}")


if __name__ == "__main__":
    asyncio.run(main())
