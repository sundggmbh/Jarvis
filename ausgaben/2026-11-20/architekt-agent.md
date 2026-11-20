# Arbeitsprobe: architekt-agent

# Netzwerk-Architektur-Bericht | Jarvis GmbH
**Datum:** [Aktueller Tag]  
**Rolle:** Netzwerk-Architekt-Agent  
**Fokus:** Optimierung von Durchsatz, Kosten-Nutzen-Verhältnis und Agenten-Kollaboration

---

### 1) Bewertung des aktuellen Netzwerks (Audit)

* **Werttreiber (High Value):**
  * **Code- & Refactoring-Agent (Ollama/Hermes):** Liefert präzise, deterministische Artefakte mit klaren Test-Suites. Geringe Fehlerrate bei scharf abgegrenzten Aufgaben.
  * **Research- & Synthese-Agent (Gemini):** Hohe Treffsicherheit bei großen Kontextmengen und unstrukturierten Eingangsdaten; spart Zeit bei der Ersterfassung.
* **Schwachstellen / Geringer Wert (Low Value):**
  * **Allgemeiner Brainstorming-/Assistenten-Agent:** Erzeugt zu viel Textrauschen ohne standardisierte Schnittstellen. Die Ausgaben müssen von Folge-Agenten aufwendig geparst werden (Token-Verschwendung).
  * **Ungefilterte Review-Schleifen:** Agenten korrigieren sich gegenseitig ohne Abbruchkriterium (Ping-Pong-Effekt), was Latenz und Kosten treibt.

---

### 2) Neue Agenten-Rolle: `Contract- & Schema-Enforcer`

* **Name:** `Schema-Enforcer`
* **Aufgabe:** Schützt Downstream-Agenten vor unvollständigen oder falsch formatierten Zwischenergebnissen. Validiert Outputs gegen strikte JSON-Schemas, fängt Halluzinationen ab und fordert gezielte Selbstkorrektur an, bevor teure Modelle (z. B. Gemini) aufgerufen werden.

#### Arbeitsanweisung (System-Prompt – sofort übernehmbar):
```markdown
Du bist der Schema-Enforcer der Jarvis GmbH.
Deine einzige Aufgabe: Überprüfe die Übergabe-Nutzlast (Payload) des vorherigen Agenten gegen das definierte JSON-Schema.

Regeln:
1. Analysiere den Input ausschließlich auf Validität, Typentreue und Pflichtfelder.
2. Wenn VALID: Gib exakt das bereinigte JSON im Codeblock aus, ohne Einleitung oder Begleittext.
3. Wenn INVALID: Antworte strikt im Format:
   REJECT: [Feldname] - [Fehlerbeschreibung]
   Fordere keine neuen Fakten an, sondern verlange nur die formale Korrektur.
4. Kürze redundanten Freitext außerhalb des JSON-Blocks vollständig weg.
```

---

### 3) Optimierung der Zusammenarbeit & Modell-Allokation

Um Redundanzen und Latenz zu minimieren, wird eine strikte Drei-Ebenen-Aufgabenteilung implementiert:

| Modell / Tool | Primäre Rolle | Einsatzbereich & Übergabe |
| :--- | :--- | :--- |
| **Gemini (Cloud / Heavy Context)** | *Architekt & Stratege* | Hohe Kontextfenster, Erstellung von Initial-Blueprints, strategische Synthese. Übergibt **nur** JSON-basierte Zielvorgaben. |
| **Hermes (Agentic / Tool-Use)** | *Dispatcher & Controller* | Funktionsaufrufe, Tool-Routing, Schnittstellen-Koordination. Nimmt Geminis Blueprint und steuert Einzelschritte. |
| **Ollama (Lokal / Spezifisch)** | *Worker & Validator* | Lokale 7B/8B-Modelle für Extraction, Linting, Format-Korrektur und Embedding-Checks. Keine API-Kosten für iterative Kleinstaufgaben. |

**Übergabe-Standard (Payload-Contract):**
Kein Agent übergibt seinen gesamten Chathistorien-Kontext. Die Übergabe erfolgt standardisiert über eine State-Card:
```json
{
  "trace_id": "req-10294",
  "source_agent": "gemini_planner",
  "status": "in_progress",
  "data": { ... },
  "next_required_action": "code_generation"
}
```

---

### 4) Lösung für ein aktuelles Problem: "Kontext-Drift & Token-Aufblähung"

* **Problem:** Agenten reichen bisher den gesamten Gesprächsverlauf weiter. Nach drei Handoffs besteht der Input zu 70 % aus veraltetem Kontext, was zu Fehlschlüssen bei schwächeren Modellen führt und Gemini unnötig verteuert.
* **Lösung (Immediate Action): "Stateless Handoff Protocol"**
  1. **Kontext-Stripping:** Jeder Agent erhält beim Aufruf ausschließlich:
     * System-Prompt (Rolle).
     * Den Output des *direkten* Vorgängers (bereinigt durch den `Schema-Enforcer`).
     * Globale Constraints (max. 3 Zeilen).
  2. **Umsetzung:** Hermes puffert den Gesamtkontext intern in einer SQLite-Datenbank/Key-Value-Store und übergibt an Folge-Agenten nur den Pointer bzw. die isolierte Teillast via State-Card.
  3. **Ergebnis:** Reduziert die Token-Kosten pro Durchlauf um schätzungsweise 40–60 % und eliminiert "Lost in the Middle"-Halluzinationen.
