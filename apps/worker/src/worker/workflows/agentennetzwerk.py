import asyncio

import mistralai.workflows as workflows
import mistralai.workflows.plugins.mistralai as workflows_mistralai
from mistralai.client.models import TextChunk, WebSearchTool
from pydantic import BaseModel, Field

MODEL = "mistral-medium-latest"
MAX_TURNS = 8


class AgentenRolle(BaseModel):
    name: str
    beschreibung: str
    auftrag: str


AGENTEN_ROLLEN: list[AgentenRolle] = [
    AgentenRolle(
        name="marktchancen-agent",
        beschreibung="Recherchiert aktuelle Marktchancen fuer KI-Dienstleistungen",
        auftrag=(
            "Du bist der Marktchancen-Agent des Jarvis-Netzwerks einer deutschen GmbH. "
            "Recherchiere im Web aktuelle Marktchancen fuer KI-gestuetzte Dienstleistungen "
            "(z. B. Content-Erstellung, Marktrecherche, Datenpflege, Lead-Qualifizierung). "
            "Nenne fuer jede Chance: Zielgruppe, Nachweis der Nachfrage, Preisniveau und "
            "warum ein kleines Team mit KI-Agenten hier schnell liefern kann. "
            "Antworte auf Deutsch, kompakt und faktenbasiert."
        ),
    ),
    AgentenRolle(
        name="verdienstmodelle-agent",
        beschreibung="Findet konkrete Moeglichkeiten, online Geld zu verdienen",
        auftrag=(
            "Du bist der Verdienstmodelle-Agent des Jarvis-Netzwerks einer deutschen GmbH. "
            "Recherchiere im Web konkrete, legale Moeglichkeiten, online Geld zu verdienen: "
            "Dienstleistungsangebote, digitale Produkte, Abonnement-Modelle, Affiliate, "
            "Marktplaetze und Plattformen. Bewerte jede Moeglichkeit nach Startaufwand, "
            "Zeit bis zum ersten Umsatz und Skalierbarkeit. Antworte auf Deutsch."
        ),
    ),
    AgentenRolle(
        name="wettbewerber-agent",
        beschreibung="Analysiert Wettbewerb und Preissetzung",
        auftrag=(
            "Du bist der Wettbewerber-Agent des Jarvis-Netzwerks einer deutschen GmbH. "
            "Recherchiere im Web, welche Anbieter und KI-Agenten-Dienstleister es in den "
            "Bereichen Recherche-as-a-Service, Content-Erstellung und Datenanalyse gibt. "
            "Nenne typische Preise, Alleinstellungsmerkmale und Luecken im Angebot, "
            "die ein neues Team besetzen kann. Antworte auf Deutsch."
        ),
    ),
    AgentenRolle(
        name="risiko-agent",
        beschreibung="Prueft rechtliche und wirtschaftliche Risiken",
        auftrag=(
            "Du bist der Risiko-Agent des Jarvis-Netzwerks einer deutschen GmbH. "
            "Recherchiere im Web rechtliche und wirtschaftliche Rahmenbedingungen fuer den "
            "Betrieb von KI-Agenten-Diensten aus Deutschland: DSGVO, Impressumspflicht, "
            "AI Act, Plattform-Nutzungsbedingungen und typische Stolperfallen bei "
            "automatisierten Diensten. Formuliere klare Handlungsempfehlungen. "
            "Antworte auf Deutsch."
        ),
    ),
]


class AgentennetzwerkInput(BaseModel):
    auftrag: str = Field(
        default=(
            "Finde konkrete, legale Wege, wie eine kleine deutsche GmbH mit einem Netzwerk "
            "aus KI-Agenten online Einnahmen erzielen kann. Priorisiere Wege mit geringem "
            "Startaufwand und schnellem ersten Umsatz."
        )
    )


class AgentenBefund(BaseModel):
    agent: str
    befund: str


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
