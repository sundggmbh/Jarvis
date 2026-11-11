import asyncio
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import mistralai
from mistralai.client.models import MessageOutputEntry, TextChunk, WebSearchTool

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.rollen import AGENTEN_ROLLEN, BERICHTS_ANWEISUNG, STANDARD_AUFTRAG, AgentenBefund, AgentenRolle  # noqa: E402

MODEL = "mistral-medium-latest"
REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"


def text_aus_antwort(antwort) -> str:
    teile = []
    for eintrag in antwort.outputs:
        if isinstance(eintrag, MessageOutputEntry):
            for inhalt in eintrag.content:
                if isinstance(inhalt, TextChunk) and inhalt.text.strip():
                    teile.append(inhalt.text.strip())
    return "\n\n".join(teile).strip()


async def agent_recherche(client: mistralai.client.Mistral, rolle: AgentenRolle, auftrag: str) -> AgentenBefund:
    antwort = await client.beta.conversations.start_async(
        model=MODEL,
        instructions=rolle.auftrag,
        inputs=auftrag,
        tools=[WebSearchTool()],
        store=False,
    )
    befund = text_aus_antwort(antwort)
    if not befund:
        raise RuntimeError(f"Agent {rolle.name} hat keinen Befund geliefert.")
    return AgentenBefund(agent=rolle.name, befund=befund)


async def bericht_konsolidieren(client: mistralai.client.Mistral, auftrag: str, befunde: list[AgentenBefund]) -> str:
    befunde_text = "\n\n".join(f"### Befund von {befund.agent}\n{befund.befund}" for befund in befunde)
    antwort = await client.beta.conversations.start_async(
        model=MODEL,
        instructions=BERICHTS_ANWEISUNG,
        inputs=f"Auftrag: {auftrag}\n\nBefunde der Agenten:\n\n{befunde_text}",
        store=False,
    )
    bericht = text_aus_antwort(antwort)
    if not bericht:
        raise RuntimeError("Berichts-Agent hat keinen Report geliefert.")
    return bericht


def report_text(auftrag: str, zeitstempel: datetime, bericht: str, befunde: list[AgentenBefund]) -> str:
    kopf = (
        f"# Jarvis Netzwerk-Bericht ({zeitstempel.strftime('%Y-%m-%d %H:%M UTC')})\n\n"
        f"**Auftrag:** {auftrag}\n\n"
        f"**Agenten:** {', '.join(befund.agent for befund in befunde)}\n\n"
        f"## Einzelbefunde\n\n"
    )
    befunde_markdown = "\n\n".join(f"### {befund.agent}\n\n{befund.befund}" for befund in befunde)
    return f"{kopf}{befunde_markdown}\n\n---\n\n{bericht}\n"


async def main() -> None:
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise SystemExit("MISTRAL_API_KEY ist nicht gesetzt. In .env oder Umgebungsvariable eintragen.")

    auftrag = " ".join(sys.argv[1:]) or STANDARD_AUFTRAG

    client = mistralai.client.Mistral(api_key=api_key)
    zeitstempel = datetime.now(timezone.utc)

    print(f"Starte {len(AGENTEN_ROLLEN)} Agenten parallel ...")
    befunde = list(
        await asyncio.gather(*(agent_recherche(client, rolle, auftrag) for rolle in AGENTEN_ROLLEN))
    )
    for befund in befunde:
        print(f"  OK {befund.agent}: {len(befund.befund)} Zeichen")

    print("Konsolidiere Bericht ...")
    bericht = await bericht_konsolidieren(client, auftrag, befunde)

    pfad = REPORTS_DIR / f"{zeitstempel.strftime('%Y-%m-%d')}-netzwerk-bericht.md"
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(report_text(auftrag, zeitstempel, bericht, befunde), encoding="utf-8")
    print(f"Bericht gespeichert: {pfad}")


if __name__ == "__main__":
    asyncio.run(main())
