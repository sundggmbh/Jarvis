# Jarvis Agentennetzwerk

Ein Netzwerk aus spezialisierten KI-Recherche-Agenten. Alle Agenten laufen **parallel**, recherchieren im Web und ihre Befunde werden zu einem Bericht mit konkreten Aufträgen konsolidiert.

Zwei Betriebsarten, gleiche Agenten:

| Betrieb | Wie | Kosten |
|---|---|---|
| **GitHub Actions** (empfohlen) | Läuft täglich automatisch, Bericht landet als Datei im Repo | GitHub Actions ist für öffentliche Repos kostenlos; Mistral-API-Kosten nach Nutzung |
| **Mistral Workflow (Studio)** | Durable Orchestrierung als Managed Deployment | Braucht einen Managed-Deployment-Slot (aktuell limitiert) |

## Agenten im Netzwerk

| Agent | Aufgabe |
|---|---|
| `marktchancen-agent` | Marktchancen für KI-Dienstleistungen |
| `verdienstmodelle-agent` | Konkrete Möglichkeiten, online Geld zu verdienen |
| `wettbewerber-agent` | Wettbewerb, Preise und Angebotslücken |
| `risiko-agent` | Rechtliche und wirtschaftliche Risiken (DSGVO, AI Act) |

### Neuen Agenten rekrutieren

In `shared/rollen.py` einen Eintrag in `AGENTEN_ROLLEN` ergänzen:

```python
AgentenRolle(
    name="neuer-agent",
    beschreibung="Kurze Rollenbeschreibung",
    auftrag="Detaillierte Anweisungen für den Agenten.",
),
```

Der neue Agent läuft automatisch in beiden Betriebsarten parallel mit allen anderen mit.

## Schnellstart: GitHub Actions (kostenlos)

1. In den Repository-Einstellungen unter **Secrets and variables → Actions** ein Secret `MISTRAL_API_KEY` anlegen (API-Key aus [console.mistral.ai](https://console.mistral.ai/)).
2. Auf der Actions-Seite den Workflow **Agentennetzwerk** per **Run workflow** starten (oder täglich 06:00 UTC automatisch).
3. Der fertige Bericht erscheint als Markdown-Datei unter `reports/` im Repository.

## Lokal ausführen

```bash
uv sync
cp .env.example .env   # MISTRAL_API_KEY setzen
uv run python scripts/agentennetzwerk.py "Optional eigener Auftrag"
```

Der Bericht wird unter `reports/` gespeichert.

## Mistral Workflow (Studio)

Der gleiche Netzwerk-Code läuft zusätzlich als Workflow `agentennetzwerk` (`apps/worker/`) mit dauerhafter Ausführung. Deployen per Managed Deployment mit Dockerfile-Pfad `deploy/docker/Dockerfile.worker`, sobald ein Deployment-Slot verfügbar ist.

## Struktur

```
shared/rollen.py                       # Agenten-Rollen (gemeinsam für beide Betriebsarten)
scripts/agentennetzwerk.py             # Standalone-Ausführung (lokal / GitHub Actions)
apps/worker/src/worker/workflows/      # Workflow-Variante (Mistral Studio)
.github/workflows/agentennetzwerk.yml  # Täglicher automatischer Lauf
deploy/docker/Dockerfile.worker        # Container für Managed Deployment
tests/                                 # Tests mit gemockten LLM-Antworten
```

## Tests

```bash
uv sync --dev
uv run pytest
```
