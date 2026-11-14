# Arbeitsprobe: architekt-agent

# Netzwerk-Architektur-Bericht | Jarvis GmbH

---

### 1. Bewertung des aktuellen Agenten-Netzwerks

* **Agenten mit hohem Wert (Behalten & Optimieren):**
  * **Planer / Orchestrator (Gemini-Basis):** Hohe strategische Treffsicherheit bei Task-Dekonstruktion und Zerlegung komplexer Workflows.
  * **Tool-Caller / Execution-Agent (Hermes-Basis):** Sehr zuverlässig bei der Ausführung von Funktionsaufrufen und der Übersetzung von Instruktionen in parametrisierte Payloads.
  * **Lokale Parser & Extraktoren (Ollama-Basis):** Effiziente, kostengünstige Vorstrukturierung unstrukturierter Rohdaten ohne Token-Kosten auf Cloud-Ebene.

* **Agenten mit geringem Wert (Überarbeiten oder Terminieren):**
  * **„General-Summarizer“-Agent (Cloud-LLM):** Verbraucht unnötig teure API-Tokens für simple Textkürzungen, die ein lokales Modell via Ollama mit gleicher Güte erledigt.
  * **Freitext-Rechercheure ohne Tool-Anbindung:** Erzeugen ohne Grounding/Search-Tools spekulative Zwischenschritte („Halluzinations-Kaskaden“) und verunreinigen den Shared Context für nachgelagerte Instanzen.

---

### 2. Neue Agenten-Rolle: *Context-Pruner & Schema-Gatekeeper (CP-Gate)*

* **Rollenname:** `Context-Pruner & Schema-Gatekeeper` (Kürzel: `CP-Gate`)
* **Aufgabe:** Prüft Zwischenergebnisse vor der Weitergabe an teurere Modelle (Gemini). Entfernt Token-Ballast, validiert die Einhaltung definierter JSON-Schemata und stoppt fehlerhafte Payloads sofort (Circuit Breaker).
* **Betriebsbasis:** Ollama (z. B. mit *Qwen2.5-Coder-7B* oder *Llama-3.1-8B-Instruct*).

#### Sofort übernehmbare Arbeitsanweisung (System-Prompt):

```markdown
Du bist der "CP-Gate"-Agent der Jarvis GmbH. Deine Aufgabe ist die strikte Filterung und Validierung von Zwischenergebnissen im Agenten-Netzwerk.

Regeln:
1. Analysiere den übergebenen Input auf das vorgegebene JSON-Zielschema.
2. Entferne jeglichen Höflichkeitstext, redundante Phrasen, Wiederholungen und System-Metadaten, die für den nächsten Bearbeitungsschritt irrelevant sind.
3. Wenn der Input das geforderte Schema nicht erfüllt oder fehlerhaft ist, antworte AUSSCHLIESSLICH mit:
   {"status": "ERROR", "reason": "<Kurze Fehlerbeschreibung>", "retry_required": true}
4. Wenn der Input valide ist, optimiere den Inhalt auf maximale Informationsdichte und antworte AUSSCHLIESSLICH im geforderten JSON-Format ohne Markdown-Wrapper oder Erklärungstext.
```

---

### 3. Vorschlag zur besseren Zusammenarbeit (Tiering & Handoff)

Um Ressourcen optimal zu nutzen und Latenzen sowie Kosten zu senken, wird eine strikte Dreiteilung der Aufgaben nach Modellanforderung etabliert:

```
[Rohdaten/Input] 
       │
       ▼
 [Ollama: Ingestion & Maskierung] 
       │ (Kompaktes JSON)
       ▼
 [Hermes: API- & Tool-Execution] 
       │ (Strukturierte Tool-Ergebnisse)
       ▼
 [Gemini: Reasoning, Synthese & Finaler Output]
```

1. **Ollama (Lokal / On-Prem):**
   * **Scope:** Lokale Vorverarbeitung, PII-Maskierung (Datenschutz), Typisierung und Schema-Validierung (`CP-Gate`).
   * **Übergabe:** Liefert striktes JSON via Message-Queue (Redis) an Hermes.
2. **Hermes (Feingetuntes Modell für Funktionsaufrufe / Local oder Host):**
   * **Scope:** Ausführung deterministischer Schritte, Datenbankabfragen, API-Trigger, Code-Execution.
   * **Übergabe:** Schreibt reine Nutzdaten (State) zurück in das Queue-Objekt; keine Freitextberichte.
3. **Gemini (Cloud / High-Reasoning):**
   * **Scope:** Erhält *ausschließlich* die fertig validierten, aggregierten Daten. Übernimmt strategisches Reasoning, Endsynthese oder Edge-Case-Bewertungen, die echtes Deep-Context-Verständnis erfordern.

---

### 4. Lösung für ein aktuelles Netzwerk-Problem: *Context Degradation & Prompt Drift*

* **Problem:** Werden Zwischenergebnisse als unformatierter Freitext von Agent zu Agent gereicht, schleichen sich Missverständnisse ein, der Kontext wird progressiv aufgebläht und nach 3–4 Handoffs halluziniert der Ziel-Agent.
* **Architektur-Lösung:** Einführung des **State-Payload-Protokolls (SPP)**:
  1. **Abschaffung von Freitext-Übergaben:** Kein Agent darf dem nächsten Agenten unstrukturierten Text weiterreichen. Jede Übergabe erfolgt über ein fixiertes Schema:
     ```json
     {
       "session_id": "uuid4",
       "task_id": "step_n",
       "facts_established": ["Fakt 1", "Fakt 2"],
       "working_data": {},
       "next_agent": "hermes_executor"
     }
     ```
  2. **Automatischer Fallback-Loop:** Schlägt die Validierung durch `CP-Gate` zweimal fehl, wird der Task nicht weitergereicht, sondern mit dem spezifischen Parsing-Fehler an den Sender zurückgewiesen, anstatt den Folge-Agenten mit inkonsistentem Kontext zu blockieren.
