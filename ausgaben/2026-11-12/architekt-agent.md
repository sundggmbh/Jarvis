# Arbeitsprobe: architekt-agent

# Tagesbericht: Optimierung des Agenten-Netzwerks
**Rolle:** Netzwerk-Architekt-Agent | Jarvis GmbH  
**Datum:** *Aktueller Systemtag*  
**Status:** Aktiv

---

### 1) Bewertung des aktuellen Agenten-Netzwerks

* **Hoher Wert:**
  * **Gemini (Architektur & Synthese):** Liefert exzellente Ergebnisse bei konzeptionellen Aufgaben mit großem Kontextfenster (Dokumentenanalyse, strategische Planung).
  * **Ollama / Lokale Modelle (Spezialisten & Code):** Unverzichtbar für schnelle, datenschutzsensible Tasks (Regex, strukturierte Extraktion, lokale Code-Reviews) ohne Token-Kosten.
* **Geringer Wert / Optimierungsbedarf:**
  * **Generalistische "Zwischen-Agenten":** Agenten, die Text lediglich zusammenfassen oder von einem Format ins nächste umformulieren, ohne semantischen Mehrwert zu schaffen, verbrauchen Latenz und Token.
  * **Hermes (Routing & Function Calling):** Funktioniert bei einfachen Tool-Calls zuverlässig, neigt jedoch bei mehrstufigen Workflows ohne striktes JSON-Schema zu Formatierungsbrüchen.

---

### 2) Neue Agenten-Rolle (Sofort einsatzbereit)

#### **Rollenname:** `Schema-Guard` (Output-Validator & Context-Trimmer)
* **Aufgabe:** Prüft Zwischenergebnisse anderer Agenten auf Validität (JSON/Typisierung), filtert redundanten Konversationsmüll (Tokens) heraus und gibt nur die bereinigte Nutzinformation an den nächsten Agenten weiter.

```markdown
### SYSTEM PROMPT: Schema-Guard
Du bist der Schema- & Konsistenz-Guard der Jarvis GmbH. 
Deine einzige Aufgabe ist die Validierung, Bereinigung und Kompression von Agenten-Zwischenergebnissen.

Regeln:
1. Prüfe den Input gegen das angegebene Zielschema (z. B. JSON-Format oder vorgegebene Markdown-Struktur).
2. Lösche sämtliche Fülltexte ("Hier ist das Ergebnis:", Höflichkeitsfloskeln, Wiederholungen der Aufgabenstellung).
3. Korrigiere fehlerhafte JSON-Syntax selbstständig.
4. Falls essenzielle Daten fehlen: Antworte AUSSCHLIESSLICH mit:
   {"status": "ERROR", "missing_fields": ["feld1", "feld2"], "raw_context": "..."}
5. Bei Erfolg: Gib AUSSCHLIESSLICH das bereinigte Zielobjekt zurück. Keine Erklärungen vor oder nach dem Block.
```

---

### 3) Zusammenarbeit & Lastverteilung (Gemini, Ollama, Hermes)

Um Redundanzen und Latenzen zu minimieren, wird die Pipeline strikt nach Stärken segmentiert:

```
[Gemini]                 [Hermes]                 [Ollama]
Strategie & Dekomposition -> Orchestrierung & Tools -> Schnelle Batch-Ausführung
       │                        │                        │
       ▼                        ▼                        ▼
(1) Erstellt Master-Plan   (2) Steuert Tool-Calls    (3) Führt Sub-Tasks lokal aus
    & JSON-Zielschema           & kontrolliert Flow      (Code-Gen, Datenextraktion)
```

**Konkrete Übergaberegeln:**
1. **Gemini $\rightarrow$ Hermes:** Gemini generiert *keinen* Freitext, sondern ein `Execution-Manifest` (Aufgaben-Array mit Input/Output-Definition).
2. **Hermes $\rightarrow$ Ollama:** Hermes ruft Ollama über eine lokale REST-API an. Übergabe erfolgt mit `temperature: 0.1` und fixiertem `format: "json"`.
3. **Hermes $\rightarrow$ Gemini:** Nach Abschluss aller Sub-Tasks aggregiert Hermes das Endergebnis und übergibt Gemini ausschließlich das End-Payload zur finalen Qualitätsprüfung/Synthese.

---

### 4) Lösung für ein Kernproblem: Kontext-Bloat & Drift

* **Problem:** Bei mehrstufigen Agenten-Workflows wird häufig die gesamte bisherige Chathistorie mitgeschleift. Folge: Nach 3–4 Iterationen verlieren Modelle den Fokus ("Lost in the Middle"), Halluzinationen steigen und Token-Kosten explodieren.
* **Lösung: "Stateless Artifact Handover" (Artefakt-Übergabe statt Historie):**
  1. **History-Drop:** Kein Agent erhält den vollständigen Chatverlauf des vorherigen Agenten.
  2. **Shared State:** Die Übergabe erfolgt über einen zentralen In-Memory-State (Key-Value-Store, z. B. Redis oder lokales JSON-Dict).
  3. Jeder Agent erhält zur Ausführung nur drei Parameter:
     * `global_goal`: Das primäre Gesamtziel (1 Satz).
     * `task_input`: Das konkrete Artefakt des Vorgängers.
     * `expected_schema`: Das vorgegebene Zielformat.

**Sofortmaßnahme:** Alle aktiven Prompts anpassen, sodass Agenten angewiesen werden, nur noch das Endergebnis als Datenartefakt auszugeben, anstatt den vorherigen Dialog zu spiegeln.
