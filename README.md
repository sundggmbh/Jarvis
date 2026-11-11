# Jarvis Agentennetzwerk

Ein Netzwerk aus spezialisierten KI-Recherche-Agenten als [Mistral Workflow](https://docs.mistral.ai/studio/workflows/overview/). Alle Agenten laufen **parallel**, recherchieren im Web und ihre Befunde werden zu einem Bericht mit konkreten Aufträgen konsolidiert.

## Agenten im Netzwerk

| Agent | Aufgabe |
|---|---|
| `marktchancen-agent` | Marktchancen für KI-Dienstleistungen |
| `verdienstmodelle-agent` | Konkrete Möglichkeiten, online Geld zu verdienen |
| `wettbewerber-agent` | Wettbewerb, Preise und Angebotslücken |
| `risiko-agent` | Rechtliche und wirtschaftliche Risiken (DSGVO, AI Act) |

### Neuen Agenten rekrutieren

In `apps/worker/src/worker/workflows/agentennetzwerk.py` einen Eintrag in `AGENTEN_ROLLEN` ergänzen:

```python
AgentenRolle(
    name="neuer-agent",
    beschreibung="Kurze Rollenbeschreibung",
    auftrag="Detaillierte Anweisungen für den Agenten.",
),
```

Der Agent wird beim nächsten Deploy automatisch parallel mit allen anderen ausgeführt.

## Struktur

```
apps/worker/src/worker/
├── entrypoints/worker.py         # Worker-Start, findet alle Workflows
└── workflows/agentennetzwerk.py  # Agenten-Rollen + Workflow
deploy/docker/Dockerfile.worker   # Container für Managed Deployment
tests/                            # Tests mit gemocktem LLM-Lauf
```

## Lokal entwickeln

```bash
uv sync --dev
cp .env.example .env   # MISTRAL_API_KEY setzen
uv run pytest
```

## Deployen

Der Workflow wird als Managed Deployment betrieben: Push nach GitHub, dann in Mistral Studio (oder per `mistral apps deploy`) mit Dockerfile-Pfad `deploy/docker/Dockerfile.worker` deployen.

Der Workflow heißt `agentennetzwerk` und nimmt optional einen Auftrag als Input:

```json
{"auftrag": "Finde konkrete Wege, online Einnahmen zu erzielen."}
```
