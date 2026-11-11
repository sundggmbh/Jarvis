from pydantic import BaseModel, Field


class AgentenRolle(BaseModel):
    name: str
    beschreibung: str
    auftrag: str


class AgentenBefund(BaseModel):
    agent: str
    befund: str


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

STANDARD_AUFTRAG = (
    "Finde konkrete, legale Wege, wie eine kleine deutsche GmbH mit einem Netzwerk aus "
    "KI-Agenten online Einnahmen erzielen kann. Priorisiere Wege mit geringem Startaufwand "
    "und schnellem ersten Umsatz."
)

BERICHTS_ANWEISUNG = (
    "Du bist der Berichts-Agent des Jarvis-Netzwerks. Erhalte die Befunde mehrerer "
    "Recherche-Agenten und erstelle daraus einen Markdown-Report auf Deutsch mit genau "
    "diesen Abschnitten: '## Zusammenfassung', '## Top-Chancen' (maximal 5, jeweils mit "
    "Startaufwand, Zeit bis zum ersten Umsatz und Schaetzung des Ertragspotenzials), "
    "'## Konkrete Auftraege' (nummerierte naechste Schritte, jeweils mit verantwortlichem "
    "Agenten) und '## Risiken'. Verfasse nichts, was nicht in den Befunden steht, und "
    "markiere Unsicherheiten als offen."
)
