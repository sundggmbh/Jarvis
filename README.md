# Jarvis Agentennetzwerk

Ein Netzwerk aus spezialisierten KI-Recherche-Agenten. Alle Agenten laufen **parallel**, recherchieren im Web (Google-Suche) und ihre Befunde werden zu einem Bericht mit konkreten Aufträgen konsolidiert.

**Betrieb über GitHub Actions – für öffentliche Repos komplett kostenlos** (Google Gemini Free Tier, täglicher Lauf, Berichte landen als Markdown im Repo).

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

Der neue Agent läuft automatisch parallel mit allen anderen mit.

## Schnellstart: GitHub Actions (kostenlos)

1. Kostenlosen Google-API-Key holen: [aistudio.google.com/apikey](https://aistudio.google.com/apikey) → „Create API key" (keine Kreditkarte nötig).
2. In den Repository-Einstellungen unter **Secrets and variables → Actions** ein Secret `GEMINI_API_KEY` anlegen.
3. Auf der Actions-Seite den Workflow **Agentennetzwerk** per **Run workflow** starten – oder täglich 06:00 UTC automatisch.
4. Der fertige Bericht erscheint als Markdown-Datei unter `reports/` im Repository.

## Lokal ausführen

```bash
cp .env.example .env   # GEMINI_API_KEY setzen
pip install google-genai pydantic
python scripts/agentennetzwerk.py "Optional eigener Auftrag"
```

## Struktur

```
shared/rollen.py                       # Agenten-Rollen (eine Quelle für alle Betriebsarten)
scripts/agentennetzwerk.py             # Ausführung (lokal / GitHub Actions, Google Gemini)
.github/workflows/agentennetzwerk.yml  # Täglicher automatischer Lauf
reports/                               # Fertige Netzwerk-Berichte
apps/worker/                           # Mistral-Workflow-Variante (optional, für Studio-Deployment)
deploy/docker/Dockerfile.worker        # Container für das Mistral Managed Deployment
tests/                                 # Tests mit gemockten LLM-Antworten
```

## Tests

```bash
pip install google-genai pydantic pytest pytest-asyncio
PYTHONPATH=".:apps/worker/src" pytest
```

## Mistral-Workflow-Variante (optional)

Der gleiche Netzwerk-Code existiert zusätzlich als Workflow `agentennetzwerk` (`apps/worker/`) für Mistral Studio mit dauerhafter Ausführung. Er wird aktiviert, sobald ein Managed-Deployment-Slot verfügbar ist (Dockerfile-Pfad: `deploy/docker/Dockerfile.worker`).
