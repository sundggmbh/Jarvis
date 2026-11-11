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

BACKEND = os.environ.get("NETZWERK_BACKEND", "gemini")
MODEL = os.environ.get("GEMINI_MODELL", "gemini-3.8-flash")
MIT_SUCHE = os.environ.get("NETZWERK_MIT_SUCHE", "0") == "1"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODELL = os.environ.get("OLLAMA_MODELL", "llama3.1:8b")
HERMES_MODELL = os.environ.get("HERMES_MODELL", "hermes3:8b")
CLOUD_BASE_URL = os.environ.get("CLOUD_BASE_URL", "https://openrouter.ai/api/v1")
CLOUD_API_KEY = os.environ.get("CLOUD_API_KEY", "")
CLOUD_MODELL = os.environ.get("CLOUD_MODELL", "meta-llama/llama-3.3-70b-instruct:free")
CLOUD2_BASE_URL = os.environ.get("CLOUD2_BASE_URL", "https://api.groq.com/openai/v1")
CLOUD2_API_KEY = os.environ.get("CLOUD2_API_KEY", "")
CLOUD2_MODELL = os.environ.get("CLOUD2_MODELL", "openai/gpt-oss-120b")
CLOUD3_BASE_URL = os.environ.get("CLOUD3_BASE_URL", "https://api.mistral.ai/v1")
CLOUD3_API_KEY = os.environ.get("CLOUD3_API_KEY", "")
CLOUD3_MODELL = os.environ.get("CLOUD3_MODELL", "mistral-small-latest")
CLOUD4_BASE_URL = os.environ.get("CLOUD4_BASE_URL", "https://api.cohere.ai/compatibility/v1")
CLOUD4_API_KEY = os.environ.get("CLOUD4_API_KEY", "")
CLOUD4_MODELL = os.environ.get("CLOUD4_MODELL", "command-r7b-12-2024")
CLOUD5_BASE_URL = os.environ.get("CLOUD5_BASE_URL", "https://integrate.api.nvidia.com/v1")
CLOUD5_API_KEY = os.environ.get("CLOUD5_API_KEY", "")
CLOUD5_MODELL = os.environ.get("CLOUD5_MODELL", "meta/llama-3.1-8b-instruct")
CLOUD6_BASE_URL = os.environ.get("CLOUD6_BASE_URL", "https://router.huggingface.co/v1")
CLOUD6_API_KEY = os.environ.get("CLOUD6_API_KEY", "")
CLOUD6_MODELL = os.environ.get("CLOUD6_MODELL", "meta-llama/Llama-3.1-8B-Instruct")

_cloud_stellen: dict[str, tuple[str, str, str]] = {
    "cloud": (CLOUD_BASE_URL, CLOUD_API_KEY, CLOUD_MODELL),
    "cloud2": (CLOUD2_BASE_URL, CLOUD2_API_KEY, CLOUD2_MODELL),
    "cloud3": (CLOUD3_BASE_URL, CLOUD3_API_KEY, CLOUD3_MODELL),
    "cloud4": (CLOUD4_BASE_URL, CLOUD4_API_KEY, CLOUD4_MODELL),
    "cloud5": (CLOUD5_BASE_URL, CLOUD5_API_KEY, CLOUD5_MODELL),
    "cloud6": (CLOUD6_BASE_URL, CLOUD6_API_KEY, CLOUD6_MODELL),
}
MAX_PARALLEL = int(os.environ.get("NETZWERK_MAX_PARALLEL", "3"))

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
AUSGABEN_DIR = REPO_ROOT / "ausgaben"

_drossel = asyncio.Semaphore(MAX_PARALLEL)
_hybrid_reihenfolge = ["gemini", *_cloud_stellen.keys(), "ollama", "hermes"]
_cloud_namen = list(_cloud_stellen.keys())
_ersatz_ketten = {
    "gemini": [*_cloud_namen, "ollama", "hermes"],
    "ollama": ["hermes", *_cloud_namen, "gemini"],
    "hermes": ["ollama", *_cloud_namen, "gemini"],
    **{
        name: ["gemini", *[n for n in _cloud_namen if n != name], "ollama", "hermes"]
        for name in _cloud_namen
    },
}
_verwendete_backends: dict[str, str] = {}
_backend_status: dict[str, bool | None] = {"ollama": None}

_bekannte_namen = sorted(rolle.name for rolle in AGENTEN_ROLLEN + GESCHAEFTS_AGENTEN)


def _primares_backend(rolle: AgentenRolle) -> str:
    if BACKEND in _hybrid_reihenfolge:
        return BACKEND
    if BACKEND == "hybrid":
        if rolle.name in _bekannte_namen:
            return _hybrid_reihenfolge[_bekannte_namen.index(rolle.name) % len(_hybrid_reihenfolge)]
        return "gemini"
    raise ValueError(f"Unbekanntes Backend: {BACKEND}")


def _system_anweisung(rolle: AgentenRolle, backend: str) -> str:
    system = rolle.auftrag
    if backend == "gemini" and not MIT_SUCHE:
        system = (
            "Hinweis: Du hast keinen Internetzugang. Arbeite mit deinem eigenen Wissen und "
            "kennzeichne veraltete oder unsichere Angaben als offen. " + system
        )
    if backend in ("ollama", "hermes", *_cloud_namen):
        system = (
            "Hinweis: Du hast keinen Internetzugang. Nutze dein eigenes Wissen "
            "und kennzeichne unsichere Angaben als offen. " + system
        )
    return system


def _tools(backend: str) -> list | None:
    if backend != "gemini" or not MIT_SUCHE:
        return None
    return [types.Tool(google_search=types.GoogleSearch())]


async def _ollama_chat(system: str, nutzer: str, modell: str = "") -> str:
    async with httpx.AsyncClient(timeout=600) as client:
        antwort = await client.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": modell or OLLAMA_MODELL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": nutzer},
                ],
                "stream": False,
            },
        )
        antwort.raise_for_status()
        return antwort.json()["message"]["content"].strip()


async def _hermes_chat(system: str, nutzer: str) -> str:
    return await _ollama_chat(system, nutzer, modell=HERMES_MODELL)


async def _openai_kompatibel_chat(base_url: str, api_key: str, modell: str, system: str, nutzer: str) -> str:
    async with httpx.AsyncClient(timeout=600) as client:
        antwort = await client.post(
            f"{base_url}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": modell,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": nutzer},
                ],
            },
        )
        antwort.raise_for_status()
        return antwort.json()["choices"][0]["message"]["content"].strip()


async def _cloud_chat(backend: str, system: str, nutzer: str) -> str:
    base_url, api_key, modell = _cloud_stellen[backend]
    return await _openai_kompatibel_chat(base_url, api_key, modell, system, nutzer)


async def _gemini_chat(system: str, nutzer: str) -> str:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    antwort = await client.aio.models.generate_content(
        model=MODEL,
        contents=nutzer,
        config=types.GenerateContentConfig(system_instruction=system, tools=_tools("gemini")),
    )
    return (antwort.text or "").strip()


async def _chat_mit(backend: str, rolle: AgentenRolle, nutzer: str) -> str:
    system = _system_anweisung(rolle, backend)
    if backend == "ollama":
        return await _ollama_chat(system, nutzer)
    if backend == "hermes":
        return await _hermes_chat(system, nutzer)
    if backend in _cloud_stellen:
        return await _cloud_chat(backend, system, nutzer)
    return await _gemini_chat(system, nutzer)


async def _backend_verfuegbar(backend: str) -> bool:
    if backend == "gemini":
        return True
    if backend in _cloud_stellen:
        return bool(_cloud_stellen[backend][1])
    if _backend_status["ollama"] is not None:
        return _backend_status["ollama"]
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            antwort = await client.get(f"{OLLAMA_URL}/api/tags")
        _backend_status["ollama"] = antwort.status_code == 200
    except Exception:
        _backend_status["ollama"] = False
    return _backend_status["ollama"]


def _ist_drossel_fehler(fehler: Exception) -> bool:
    text = str(fehler).upper()
    return "429" in text or "EXHAUSTED" in text or "RATE" in text or "QUOTA" in text


def _kurz(fehler: Exception) -> str:
    return str(fehler).replace("\n", " ")[:200]


async def frage_agent(rolle: AgentenRolle, nutzer: str) -> str:
    primar = _primares_backend(rolle)
    plan: list[tuple[str, int]] = [(primar, 4)]
    for ersatz in _ersatz_ketten.get(primar, []):
        if await _backend_verfuegbar(ersatz):
            plan.append((ersatz, 1))

    letzter_fehler: Exception | None = None
    for backend, max_versuche in plan:
        for versuch in range(max_versuche):
            try:
                async with _drossel:
                    text = await _chat_mit(backend, rolle, nutzer)
                _verwendete_backends[rolle.name] = backend
                return text
            except Exception as fehler:
                letzter_fehler = fehler
                if versuch + 1 < max_versuche:
                    pause = 30 * (versuch + 1) if _ist_drossel_fehler(fehler) else 5 * (versuch + 1)
                    print(
                        f"  {rolle.name}: {backend} fehlgeschlagen ({type(fehler).__name__}: {_kurz(fehler)}), "
                        f"wiederhole in {pause}s ..."
                    )
                    await asyncio.sleep(pause)
    assert letzter_fehler is not None
    raise letzter_fehler


async def agent_recherche(rolle: AgentenRolle, auftrag: str) -> AgentenBefund:
    text = (await frage_agent(rolle, auftrag)).strip()
    if not text:
        raise RuntimeError(f"Agent {rolle.name} hat keinen Befund geliefert.")
    return AgentenBefund(agent=rolle.name, befund=text)


MAX_BEFUND_ZEICHEN = int(os.environ.get("NETZWERK_MAX_BEFUND_ZEICHEN", "5000"))
MAX_BEFUNDE_GESAMT = int(os.environ.get("NETZWERK_MAX_BEFUNDE_GESAMT", "22000"))


def _gekuerzt(text: str, maximum: int) -> str:
    if len(text) <= maximum:
        return text
    return text[:maximum] + " ... [gekuerzt, Volltext siehe Einzelbefunde]"


async def bericht_konsolidieren(auftrag: str, befunde: list[AgentenBefund]) -> str:
    berichts_rolle = AgentenRolle(
        name="bericht-agent", beschreibung="Konsolidiert Befunde", auftrag=BERICHTS_ANWEISUNG
    )
    teile: list[str] = []
    gesamt = 0
    for befund in befunde:
        stueck = _gekuerzt(befund.befund, MAX_BEFUND_ZEICHEN)
        if gesamt + len(stueck) > MAX_BEFUNDE_GESAMT:
            stueck = _gekuerzt(stueck, max(500, MAX_BEFUNDE_GESAMT - gesamt))
        gesamt += len(stueck)
        teile.append(f"### Befund von {befund.agent}\n{stueck}")
    befunde_text = "\n\n".join(teile)
    bericht = (await frage_agent(
        berichts_rolle, f"Auftrag: {auftrag}\n\nBefunde der Agenten (gekuerzt):\n\n{befunde_text}"
    )).strip()
    if not bericht:
        raise RuntimeError("Berichts-Agent hat keinen Report geliefert.")
    return bericht


def report_text(
    auftrag: str,
    zeitstempel: datetime,
    bericht: str,
    befunde: list[AgentenBefund],
    fehler: list[tuple[str, str]] | None = None,
) -> str:
    backends = ", ".join(f"{agent}: {backend}" for agent, backend in sorted(_verwendete_backends.items()))
    kopf = (
        f"# Jarvis Netzwerk-Bericht ({zeitstempel.strftime('%Y-%m-%d %H:%M UTC')})\n\n"
        f"**Backend-Modus:** {BACKEND}\n\n"
        f"**Genutzte Backends:** {backends or 'unbekannt'}\n\n"
        f"**Auftrag:** {auftrag}\n\n"
        f"**Agenten:** {', '.join(befund.agent for befund in befunde)}\n\n"
    )
    if fehler:
        fehlertext = ", ".join(f"{name} ({art})" for name, art in fehler)
        kopf += f"**Fehlgeschlagene Agenten:** {fehlertext}\n\n"
    kopf += "## Einzelbefunde\n\n"
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

    async def gestaffelt(index: int, rolle: AgentenRolle) -> tuple[str, Path]:
        await asyncio.sleep(index * 15)
        return await eine(rolle)

    ergebnisse = await asyncio.gather(
        *(gestaffelt(index, rolle) for index, rolle in enumerate(GESCHAEFTS_AGENTEN)),
        return_exceptions=True,
    )
    proben: list[tuple[str, Path]] = []
    for rolle, ergebnis in zip(GESCHAEFTS_AGENTEN, ergebnisse):
        if isinstance(ergebnis, BaseException):
            print(f"  WARNUNG Arbeitsprobe {rolle.name} fehlgeschlagen: {type(ergebnis).__name__}")
            continue
        proben.append(ergebnis)
    return proben


async def main() -> None:
    if BACKEND in ("gemini", "hybrid") and not os.environ.get("GEMINI_API_KEY"):
        if BACKEND == "gemini":
            raise SystemExit("GEMINI_API_KEY ist nicht gesetzt (oder NETZWERK_BACKEND=ollama nutzen).")
        print("Hinweis: Kein GEMINI_API_KEY gesetzt - im Hybrid-Modus uebernehmen die anderen Backends.")
    if BACKEND in _cloud_stellen and not _cloud_stellen[BACKEND][1]:
        raise SystemExit(f"API-Schluessel fuer {BACKEND} ist nicht gesetzt (oder NETZWERK_BACKEND=ollama/hermes nutzen).")

    auftrag = " ".join(sys.argv[1:]) or STANDARD_AUFTRAG
    zeitstempel = datetime.now(timezone.utc)

    print(f"Backend-Modus: {BACKEND} | {len(AGENTEN_ROLLEN)} Recherche- + {len(GESCHAEFTS_AGENTEN)} Geschaefts-Agenten")

    if os.environ.get("NETZWERK_MIT_PROBEN", "1") == "1":
        proben = await produziere_arbeitsproben(zeitstempel)
        for name, pfad in proben:
            print(f"  Arbeitsprobe {name}: {pfad}")
    else:
        print("Arbeitsproben uebersprungen (NETZWERK_MIT_PROBEN=0) - spart Google-Kontingent.")

    print(f"Starte {len(AGENTEN_ROLLEN)} Recherche-Agenten parallel ...")

    async def recherchiert(index: int, rolle: AgentenRolle) -> AgentenBefund:
        await asyncio.sleep(index * 15)
        return await agent_recherche(rolle, auftrag)

    ergebnisse = await asyncio.gather(
        *(recherchiert(index, rolle) for index, rolle in enumerate(AGENTEN_ROLLEN)),
        return_exceptions=True,
    )
    befunde: list[AgentenBefund] = []
    fehler: list[tuple[str, str]] = []
    for rolle, ergebnis in zip(AGENTEN_ROLLEN, ergebnisse):
        if isinstance(ergebnis, BaseException):
            fehler.append((rolle.name, type(ergebnis).__name__))
            print(f"  FEHLER {rolle.name}: {type(ergebnis).__name__}: {_kurz(ergebnis)}")
        else:
            befunde.append(ergebnis)
            print(f"  OK {ergebnis.agent}: {len(ergebnis.befund)} Zeichen")

    if not befunde:
        raise SystemExit("Alle Recherche-Agenten sind fehlgeschlagen - kein Bericht erstellt.")

    print("Konsolidiere Bericht ...")
    try:
        bericht = await bericht_konsolidieren(auftrag, befunde)
    except Exception as fehler_konsolidierung:
        print(f"  WARNUNG Konsolidierung fehlgeschlagen: {type(fehler_konsolidierung).__name__} - nutze Einzelbefunde.")
        bericht = "Der Berichts-Agent ist ausgefallen; unten stehen die unverkuerzten Einzelbefunde."

    pfad = REPORTS_DIR / f"{zeitstempel.strftime('%Y-%m-%d')}-netzwerk-bericht.md"
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(report_text(auftrag, zeitstempel, bericht, befunde, fehler), encoding="utf-8")
    print(f"Bericht gespeichert: {pfad}")

    print("Backend-Verteilung:", ", ".join(f"{a}={b}" for a, b in sorted(_verwendete_backends.items())))


if __name__ == "__main__":
    asyncio.run(main())
