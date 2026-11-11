# Jarvis Agentennetzwerk

Ein Netzwerk aus spezialisierten KI-Recherche-Agenten. Alle Agenten laufen **parallel**, recherchieren im Web (Google-Suche) und ihre Befunde werden zu einem Bericht mit konkreten Aufträgen konsolidiert.

**Betrieb über GitHub Actions – für öffentliche Repos komplett kostenlos** (Google Gemini Free Tier, täglicher Lauf, Berichte landen als Markdown im Repo).

> **Hinweis zur Websuche:** Im kostenlosen Gemini-Tarif ist die Live-Websuche (Grounding) nicht enthalten. Standardmäßig arbeiten die Agenten daher mit ihrem eigenen Wissen und kennzeichnen Unsicherheiten. Wer die Live-Websuche zuschalten will, richtet in Google eine Zahlungsmethode ein und setzt die Variable `NETZWERK_MIT_SUCHE=1` (Repository → Settings → Secrets and variables → Actions → **Variables**).

## Agenten im Netzwerk

**Recherche-Agenten** (täglicher Lagebericht, Ergebnisse in `reports/`):

| Agent | Aufgabe |
|---|---|
| `marktchancen-agent` | Marktchancen für KI-Dienstleistungen |
| `verdienstmodelle-agent` | Konkrete Möglichkeiten, online Geld zu verdienen |
| `wettbewerber-agent` | Wettbewerb, Preise und Angebotslücken |
| `risiko-agent` | Rechtliche und wirtschaftliche Risiken (DSGVO, AI Act) |

**Geschäfts-Agenten** (fertige Arbeitsproben, Ergebnisse in `ausgaben/` zur Freigabe):

| Agent | Liefert täglich |
|---|---|
| `dossier-agent` | Ein verkaufsfertiges Muster-Dossier (400–1.200 € Produkt) |
| `content-agent` | 5 LinkedIn-Beiträge + Newsletter-Probe (800–2.000 €/Monat Produkt) |
| `katalog-agent` | Produkttext-Proben Vorher/Nachher (1.500–6.000 €/Projekt) |
| `automatisierungs-agent` | Komplettes Angebots-Paket für KMU (2.000–10.000 € Setup) |
| `akquise-agent` | Zielgruppen-Profile und Anschreiben-Vorlagen (nur Vorbereitung, kein Versand) |
| `architekt-agent` | Baut das Netzwerk weiter aus: neue Rollen, Zusammenarbeit, Problemlösungen |

### Neuen Agenten rekrutieren

In `shared/rollen.py` einen Eintrag in `AGENTEN_ROLLEN` (Recherche) oder `GESCHAEFTS_AGENTEN` (Arbeitsproben) ergänzen:

```python
AgentenRolle(
    name="neuer-agent",
    beschreibung="Kurze Rollenbeschreibung",
    auftrag="Detaillierte Anweisungen für den Agenten.",
),
```

Der neue Agent läuft automatisch parallel mit allen anderen mit.

## Freigabe-Prozess (Automatisierungsgrenze)

Die Agenten produzieren **vollautomatisch** Arbeitsproben und Berichte. Was die Agenten bewusst **nicht** tun: E-Mails an Kunden senden, Verträge schließen, Rechnungen stellen. Alles landet zur **Freigabe** im Repository (`ausgaben/`), ein Mensch entscheidet über den Versand – das ist rechtlich zwingend (UWG § 7 Spam-Verbot, Haftung für KI-Outputs).

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

## Vollständig lokal und netzunabhängig (Ollama)

Das Netzwerk läuft auch komplett offline auf dem eigenen Rechner – kostenlos und ohne jeden Cloud-Anbieter:

1. [Ollama](https://ollama.com/download) installieren.
2. Ein Modell laden: `ollama pull llama3.1:8b`
3. Netzwerk lokal starten:

```bash
NETZWERK_BACKEND=ollama python scripts/agentennetzwerk.py
```

Andere Modelle: `OLLAMA_MODELL=llama3.1:8b` (oder `qwen2.5:14b` für bessere Qualität, braucht mehr RAM). Hinweis: Lokale Modelle sind schwächer als Gemini – gut für Texte und Struktur, schwächer bei Fakten.

## Hermes als drittes Backend

[Hermes](https://ollama.com/library/hermes3) ist ein freies Modell von Nous Research und läuft wie Ollama komplett lokal – das Netzwerk kann Aufträge also auf drei Backends verteilen: **Gemini (Internet) + Ollama (lokal) + Hermes (lokal)**. Fällt ein Backend aus, springt die Kette automatisch weiter: Gemini → Ollama → Hermes.

1. Hermes-Modell laden: `ollama pull hermes3:8b`
2. Netzwerk mit Hermes als einzigem Backend starten:

```bash
NETZWERK_BACKEND=hermes python scripts/agentennetzwerk.py
```

3. Oder alle drei gleichzeitig nutzen (Hybrid über drei Backends):

```bash
NETZWERK_BACKEND=hybrid python scripts/agentennetzwerk.py
```

Anderes Hermes-Modell: `HERMES_MODELL=hermes3:8b` (Umgebungsvariable).

## Telegram-Fernsteuerung (Handy → Agenten)

Mit einem Telegram-Bot kann das Netzwerk vom Android-Handy aus gesteuert werden – kostenlos:

1. In Telegram nach **@BotFather** suchen, `/newbot` senden, Namen vergeben, den **Bot-Token** notieren.
2. Einen GitHub-Token erstellen: [github.com/settings/tokens](https://github.com/settings/tokens) → „Generate new token (classic)“ → Häkchen bei **repo** und **workflow** → Token notieren.
3. Auf dem Windows-PC starten:

```bash
pip install httpx
set TELEGRAM_BOT_TOKEN=<Bot-Token von BotFather>
set GITHUB_TOKEN=<GitHub-Token>
python scripts/telegram_bot.py
```

4. Den eigenen Bot in Telegram öffnen, es funktionieren:

| Befehl | Wirkung |
|---|---|
| `/status` | Zeigt, ob die Agenten gerade arbeiten (letzte 3 Läufe) |
| `/bericht` | Startet einen vollen Netzwerk-Lauf (Arbeitsproben + Bericht) |
| `/auftrag <Text>` | Gibt den Agenten einen eigenen Auftrag |

Der Bot muss auf dem PC laufen (Fenster offen lassen). Er schickt die Aufträge an GitHub, die Agenten laufen dort in der Cloud – das Handy braucht also nur Telegram.

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
