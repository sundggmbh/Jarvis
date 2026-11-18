# Arbeitsprobe: architekt-agent

# Tagesbericht: Optimierung des Jarvis-Agenten-Netzwerks
**Rolle:** Netzwerk-Architekt-Agent  
**Datum:** [Aktueller Tag]  
**Status:** Aktiv / Kontinuierliche Optimierung

---

### 1) Bewertung des aktuellen Netzwerks

* **Werttreiber (High Value):**
  * **Gemini (Cloud / Heavy Reasoning):** Liefert exzellente Ergebnisse bei Architekturplanung, komplexer Systemanalyse und der finalen Synthese unstrukturierter Daten.
  * **Hermes (Tool-Use / Function Calling):** Zuverlässig als Interface-Agent für Schnittstellen und strukturierte Tool-Aufrufe; minimale Ausfallrate bei JSON-Payloads.
* **Schwachstellen / Geringer Wert (Low Value):**
  * **Ungezielte Review-Schleifen:** Agenten, die rein als „Kritiker“ ohne strikte Prüfmatrix arbeiten, blähen den Kontext auf, ohne messbare Fehler zu korrigieren.
  * **Ollama im Prompt-Chaining (ohne Schema):** Lokale Modelle driften ab, wenn sie langen Chat-Historien ausgesetzt werden; hoher Nachbearbeitungsaufwand bei unstrukturiertem Text.

---

### 2) Neue Agenten-Rolle: `Context-Pruner & Schema-Enforcer`

* **Name:** `StateGuard-Agent`
* **Aufgabe:** Minimierung von Context-Rot (Kontextvergiftung) und strikte Typisierung an Schnittstellen zwischen Agentenübergaben.
* **Arbeitsanweisung (System-Prompt – sofort übernehmbar):**

```markdown
Du bist der StateGuard-Agent im Jarvis-Netzwerk.
Deine einzige Aufgabe ist es, Zwischenergebnisse vor der Weitergabe an das nächste Modell radikal zu verdichten und in ein striktes JSON-Format zu überführen.

Regeln:
1. Entferne Höflichkeitsfloskeln, Wiederholungen und vage Spekulationen.
2. Extrahiere ausschließlich Fakten, Code-Artefakte, Fehlermeldungen und explizite Entscheidungen.
3. Gib NIEMALS Fliesstext ausserhalb des JSON-Blocks aus.

Antwort-Schema:
{
  "task_id": "string",
  "status": "in_progress" | "blocked" | "completed",
  "core_facts": ["string"],
  "artifacts": { "key": "value" },
  "next_action_required": "string"
}
```

---

### 3) Bessere Zusammenarbeit: Orchestrierung (Gemini, Ollama, Hermes)

Um Tokenkosten zu senken, Latenz zu minimieren und maximale Präzision zu erreichen, gilt folgende Aufgabenteilung:

```
[Input] -> [Ollama: Triage & Filter] -> [Hermes: Tool Execution] -> [Gemini: Deep Synthesis] -> [Output]
```

1. **Ollama (Local / Fast / Privacy):**
   * **Aufgabe:** Erste Instanz. Regex-Matching, Relevanzprüfung, Dokumenten-Chunking und Vorfilterung von Rohdaten (z. B. Logs, E-Mails).
   * **Übergabe:** Übergibt ausschließlich relevante Text-Snippets (max. 500 Tokens) an Hermes.
2. **Hermes (Function Calling & Action):**
   * **Aufgabe:** Ruft APIs auf, führt DB-Queries aus und validiert externe Rückmeldungen.
   * **Übergabe:** Übergibt die bereinigten API-Returns strukturiert an Gemini.
3. **Gemini (High-Level Reasoning & Strategie):**
   * **Aufgabe:** Löst Edge Cases, bewertet Zielkonflikte und generiert die finale Antwort bzw. den produktiven Code.
   * **Übergabe:** Schickt das Endergebnis direkt an den User oder stößt über Hermes Aktionen an.

---

### 4) Lösung für ein aktuelles Netzwerk-Problem: *Context Drift & Latenz-Explosion*

* **Problem:** Agenten übergeben vollständige Chat-Historien hin und her. Dies führt zu Context Pollution (Modelle vergessen die Originalaufgabe) und exponentiell steigenden API-Latenzen.
* **Lösung: „Contract-First Handoff“ (State Machine):**
  1. **Kein Chat-Verlauf bei Übergaben:** Agenten erhalten **nur** den System-Prompt + den validierten State des `StateGuard-Agent` (siehe Punkt 2), niemals die gesamte Historie.
  2. **Strict Timeouts & Fallback:** Antwortet ein lokales Ollama-Modell nicht innerhalb von 4 Sekunden, übernimmt direkt Hermes mit einem schlankeren Tool-Aufruf.
  3. **Dead-Letter-Queue:** Schlägt eine Agenten-Antwort 2x wegen Schema-Verletzung fehl, wird der Task an Gemini zur Fehlerbehebung eskaliert, statt in einer Endlosschleife zu verharren.
