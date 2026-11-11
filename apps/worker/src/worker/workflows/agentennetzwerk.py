import asyncio

import mistralai.workflows as workflows
import mistralai.workflows.plugins.mistralai as workflows_mistralai
from mistralai.client.models import TextChunk, WebSearchTool
from pydantic import BaseModel, Field

from shared.rollen import AGENTEN_ROLLEN, AgentenBefund, AgentenRolle

MODEL = "mistral-medium-latest"
MAX_TURNS = 8


class AgentennetzwerkInput(BaseModel):
    auftrag: str = Field(
        default=(
            "Finde konkrete, legale Wege, wie eine kleine deutsche GmbH mit einem Netzwerk "
            "aus KI-Agenten online Einnahmen erzielen kann. Priorisiere Wege mit geringem "
            "Startaufwand und schnellem ersten Umsatz."
        )
    )


class NetzwerkBericht(BaseModel):
    auftrag: str
    bericht: str
    einzelbefunde: list[AgentenBefund]


def _text_aus_outputs(outputs: list) -> str:
    return "\n\n".join(
        output.text for output in outputs if isinstance(output, TextChunk) and output.text.strip()
    ).strip()


@workflows.activity()
async def agent_recherche(rolle: AgentenRolle, auftrag: str) -> AgentenBefund:
    agent = workflows_mistralai.Agent(
        model=MODEL,
        name=rolle.name,
        description=rolle.beschreibung,
        instructions=rolle.auftrag,
        tools=[WebSearchTool()],
    )
    outputs = await workflows_mistralai.Runner.run(
        agent=agent,
        inputs=auftrag,
        session=workflows_mistralai.RemoteSession(),
        max_turns=MAX_TURNS,
    )
    befund = _text_aus_outputs(outputs)
    if not befund:
        raise RuntimeError(f"Agent {rolle.name} hat keinen Befund geliefert.")
    return AgentenBefund(agent=rolle.name, befund=befund)


@workflows.activity()
async def bericht_konsolidieren(auftrag: str, befunde: list[AgentenBefund]) -> str:
    agent = workflows_mistralai.Agent(
        model=MODEL,
        name="bericht-agent",
        description="Konsolidiert Agenten-Befunde zu einem Netzwerk-Report",
        instructions=(
            "Du bist der Berichts-Agent des Jarvis-Netzwerks. Erhalte die Befunde mehrerer "
            "Recherche-Agenten und erstelle daraus einen Markdown-Report auf Deutsch mit "
            "genau diesen Abschnitten: '## Zusammenfassung', '## Top-Chancen' (maximal 5, "
            "jeweils mit Startaufwand, Zeit bis zum ersten Umsatz und Schaetzung des "
            "Ertragspotenzials), '## Konkrete Auftraege' (nummerierte naechste Schritte, "
            "jeweils mit verantwortlichem Agenten) und '## Risiken'. Verfasse nichts, was "
            "nicht in den Befunden steht, und markiere Unsicherheiten als offen."
        ),
    )
    befunde_text = "\n\n".join(
        f"### Befund von {befund.agent}\n{befund.befund}" for befund in befunde
    )
    outputs = await workflows_mistralai.Runner.run(
        agent=agent,
        inputs=f"Auftrag: {auftrag}\n\nBefunde der Agenten:\n\n{befunde_text}",
        session=workflows_mistralai.RemoteSession(),
        max_turns=2,
    )
    bericht = _text_aus_outputs(outputs)
    if not bericht:
        raise RuntimeError("Berichts-Agent hat keinen Report geliefert.")
    return bericht


@workflows.workflow.define(
    name="agentennetzwerk",
    workflow_display_name="Jarvis Agentennetzwerk",
    workflow_description=(
        "Laesst mehrere spezialisierte Recherche-Agenten parallel laufen und konsolidiert "
        "ihre Befunde zu einem Bericht mit konkreten Auftraegen."
    ),
)
class AgentennetzwerkWorkflow:
    @workflows.workflow.entrypoint
    async def run(self, params: AgentennetzwerkInput) -> NetzwerkBericht:
        befunde = list(
            await asyncio.gather(
                *(agent_recherche(rolle, params.auftrag) for rolle in AGENTEN_ROLLEN)
            )
        )
        bericht = await bericht_konsolidieren(params.auftrag, befunde)
        return NetzwerkBericht(auftrag=params.auftrag, bericht=bericht, einzelbefunde=befunde)
