# Arbeitsprobe: architekt-agent

# Architektur-Report: Jarvis Agenten-Netzwerk

## 1. Bewertung des aktuellen Netzwerks

* **Werttreiber (High Value):**
  * **Synthese- & Strategie-Agenten (Gemini):** Hoher Durchsatz bei großen Kontexten; ideal für die Vorfilterung komplexer Aufgaben und strategische Zusammenfassungen.
  * **Lokale Ausführungs-Agenten (Ollama / z. B. Qwen/Llama):** Exzellent für datensensible, repetitive Task-Pipelines (z. B. Log-Parsing, PII-Maskierung) ohne API-Kosten oder Latenzverlust durch externe Hops.
  * **Tool-Use-Agenten (Hermes):** Zuverlässig bei striktem Function-Calling und deterministischer JSON-Generierung.

* **Flaschenhälse & Defizite (Low Value):**
  * **Generische Chat-Reviewer:** Agenten ohne klar definiertes Schema liefern oft nur redundantes "Lob" statt harter Validierung. Sie verbrennen Token ohne Qualitätsgewinn.
  * **Unstrukturierte Zwischenschritte:** Freitext-Übergaben zwischen Agenten führen zu Informationsverlust (*Context Drift*) und Halluzinationen in Folge-Prompts.

---

## 2. Neuer Rollenvorschlag: *Schema- & Pipeline-Guard (SPG)*

* **Name:** `Schema- & Pipeline-Guard (SPG)`
* **Aufgabe:** Dient als deterministischer Checkpoint zwischen Analyse- und Ausführungsagenten. Validiert Outputs gegen strikte JSON-Schemas, schneidet Kontextmüll ab und verhindert fehlerhafte State-Übergaben.
* **Arbeitsanweisung (System-Prompt – sofort übernehmbar):**

```markdown
Du bist der Schema- & Pipeline-Guard (SPG) der Jarvis GmbH.
Deine einzige Aufgabe: Validiere den Input gegen das definierte Zielschema und bereinige den Kontext.

Regeln:
1. Prüfe, ob alle Pflichtfelder vorhanden und typkorrekt sind.
2. Entferne jeglichen Konversationsballast (z. B. "Hier ist das Ergebnis:", Höflichkeitsfloskeln).
3. Wenn valide: Gib AUSSCHLIESSLICH das bereinigte JSON-Objekt zurück. Keine Erklärungen, kein Markdown-Wrapping (außerhalb des geforderten Code-Blocks).
4. Wenn invalide: Gib ein JSON mit folgendem Schema zurück:
   {"status": "ERROR", "missing_fields": [...], "rejected_input": "..."}
5. Maximiere Informationsdichte; kürze redundante Textpassagen in String-Feldern auf Kernaussagen.
```

---

## 3. Bessere Zusammenarbeit & Orchestrierung

### Modell-Aufgabenteilung (Tiered Routing)
* **Phase 1: Strategie & Ingestion → Gemini (Cloud)**
  * Verarbeitet große, unstrukturierte Inputs (Dokumente, Briefings).
  * Erstellt ein grobes Konzept und zerlegt Aufgaben in Teil-Tasks.
* **Phase 2: Strukturierung & Function-Call → Hermes (Bridge)**
  * Transformiert Geminis Freitext in validierte Funktionsaufrufe und strukturierte Zwischen-Payloads (JSON).
* **Phase 3: Determinismus & Datenschutz → Ollama (Lokal)**
  * Führt isolierte Aktionen auf internen Systemen aus (Code-Lauf, Datei-Operationen, DB-Queries), verarbeitet sensible Daten ohne Abfluss.

### Übergabeprotokoll (State Handover)
* **Verbot von Full-History-Forwarding:** Kein Weiterleiten des gesamten Chat-Verlaufs an Folge-Agenten.
* **Minimal Payload Format:**
```json
{
  "task_id": "uuid4",
  "source_agent": "gemini-core",
  "target_agent": "hermes-worker",
  "payload": { "data": "..." },
  "context_summary": "1-3 Kernsätze zum Ziel"
}
```

---

## 4. Problemlösung: Endlosschleifen bei Korrektur-Loops

* **Problem:** Agent A (Generierung) und Agent B (Kritik) geraten bei Feedback-Schleifen in Endlos-Diskussionen oder verschlimmbessern funktionierenden Code/Text (*Degenerative Reasoning*).
* **Lösung: „Max-2-Hop & Delta-Only“-Regel**
  1. **Hard-Cap:** Maximal zwei Iterationen zwischen Ersteller und Kritiker.
  2. **Delta-Feedback:** Der Prüf-Agent darf keinen Freitext-Rant senden, sondern muss ein strukturiertes Differenz-Objekt liefern (Fehlerzeile + geforderter Fix).
  3. **Fallback:** Scheitert der zweite Versuch, wird der Task automatisch an den Orchestrator eskaliert (State: `ESCALATED_TO_HUMAN_OR_GEMINI_MASTER`), statt weitere Sub-Loops zu spawnen.
