# Arbeitsprobe: architekt-agent

# Netzwerk-Architektur-Bericht | Jarvis GmbH
**Datum:** [Aktueller Tag]  
**Architekt:** Netzwerk-Architekt-Agent  

---

### 1) Bewertung des aktuellen Agenten-Netzwerks

* **Hoher Wert:**
  * **Dev/Coding-Agent (Hermes/Gemini):** Hoher Durchsatz bei Refactorings und API-Anbindungen.
  * **Research-Agent (Gemini):** Stark bei der Verdichtung großer Kontextfenster und Quellensynthesen.
* **Geringer Wert / Optimierungsbedarf:**
  * **Generischer Review-Agent:** Liefert oft oberflächliches Feedback („Sieht gut aus, aber achte auf Tests“) ohne eigene Korrektur-Aktion; blockiert Pipelines zeitlich, ohne Fehler sicher abzufangen.
  * **Unstrukturierte Zwischen-Zusammenfasser:** Verdichten Freitext in neuen Freitext, was zu Context-Drift und Informationsverlust führt.

---

### 2) Neue Agenten-Rolle: `Payload-Validator-Agent`

* **Name:** `Payload-Validator` (Gatekeeper)
* **Aufgabe:** Schnittstellenkontrolle zwischen sequenziellen Agentenschritten. Prüft, ob der Output von Agent $N$ dem erwarteten Schema für Agent $N+1$ entspricht. Verhindert Kaskadenfehler und Token-Verschwendung.
* **Arbeitsanweisung (System-Prompt, sofort einsetzbar):**

```text
Du bist der Payload-Validator-Agent der Jarvis GmbH.
Deine einzige Aufgabe: Validiere den übergebenen Input strikt gegen das geforderte Zielschema (JSON-Schema oder strukturierter Markdown-Contract).

Regeln:
1. Prüfe, ob alle Pflichtfelder vorhanden, typkorrekt und nicht-leer sind.
2. Wenn valide: Antworte AUSSCHLIESSLICH mit:
   {"status": "VALID", "sanitized_payload": <input_data>}
3. Wenn invalide: Führe KEINE Halluzinationen oder Annahmen durch. Antworte mit:
   {"status": "INVALID", "errors": ["präzise Fehlermeldung 1", "Fehlermeldung 2"], "raw_snippet": "<fehlerhafter Ausschnitt>"}
4. Gib niemals Höflichkeitsfloskeln, Markdown-Ticks (außer im JSON-Format) oder Erklärungen ab.
```

---

### 3) Zusammenarbeit & Modell-Allokation (Gemini, Ollama, Hermes)

Um Latenz und Kosten zu senken, wird eine dreistufige Pipeline etabliert:

| Modell-Instanz | Zugewiesene Rolle | Begründung & Übergabe |
| :--- | :--- | :--- |
| **Ollama** *(lokal, z.B. Mistral/Llama-3-8B)* | **Klassifizierung, Extraktion, Sensible Daten** | Filtert PII/DSGVO-Daten lokal heraus, normiert Rohtexte in JSON. Sehr schnell, keine API-Kosten. |
| **Hermes** *(Fine-Tuned Function Caller)* | **Router & Dispatcher (Orchestrierung)** | Entscheidet anhand des JSON-Schemas über den nächsten Task und stößt Tool-Calls/Sub-Agenten an. |
| **Gemini** *(Cloud, großes Kontextfenster)* | **Tiefe Synthese & Komplexe Code-Architektur** | Erhält nur noch kuratierte, vorverarbeitete Payloads. Generiert finale Artefakte/Strategien. |

**Protokoll für Zwischenergebnisse:**
* **Kein Freitext-Chat zwischen Agenten:** Austausch erfolgt zwingend über ein State-Dictionary (`{"task_id": "...", "step": 2, "data": {...}}`).
* Prosa ist nur für den Endnutzer bestimmt; die interne Pipeline kommuniziert strikt typisiert.

---

### 4) Lösung für ein aktuelles Kernproblem: *Context Drift & Halluzinations-Kaskaden*

* **Problem:** Agent A generiert Fließtext mit Annahmen. Agent B interpretiert diese Annahmen als Fakten. Nach drei Schritten weicht das Ergebnis drastisch vom User-Prompt ab (Context Drift).
* **Lösung: „Contract-First State Passing“**
  1. **Source-of-Truth fixieren:** Der ursprüngliche User-Prompt wird unveränderlich im Root-Key `root_intent` jedes Payloads mitgeführt.
  2. **Diff-Verfahren statt Re-Write:** Nachfolgende Agenten dürfen den State nicht neu formulieren, sondern nur definierte Felder anhängen (Append-Only per JSON-Patch).
  3. **Abbruch-Trigger:** Erkennt der `Payload-Validator` eine semantische Abweichung vom `root_intent`, stoppt die Pipeline sofort und wirft den Schritt mit einer `Retry-Directive` an denselben Agenten zurück, statt fehlerhafte Daten weiterzureichen.
