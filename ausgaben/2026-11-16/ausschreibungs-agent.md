# Arbeitsprobe: ausschreibungs-agent

# Arbeitsprobe: Ausschreibungs-Recherche & Angebots-Skizze
**Rolle:** Ausschreibungs-Agent, Jarvis GmbH  
**Status:** Interner Bericht / Entwurf (Keine verbindliche Abgabe)

---

## 1. Fünf typische Portale für öffentliche Ausschreibungen in Deutschland

1. **e-Vergabe des Bundes ([evergabe-online.de](https://www.evergabe-online.de))**
   * *Fokus:* Zentrale Vergabeplattform des Bundes (Beschaffungsamt des BMI, Bundeswehr, Bundesnetzagentur etc.).
   * *Bedeutung:* Primäre Quelle für bundesweite IT- und Digitalisierungsprojekte.
2. **TED – Tenders Electronic Daily ([ted.europa.eu](https://ted.europa.eu))**
   * *Fokus:* EU-weite Bekanntmachungsplattform für Ausschreibungen oberhalb der EU-Schwellenwerte.
   * *Bedeutung:* Auch deutsche Behörden (Bund, Länder, Großstädte) müssen hier IT-Aufträge ab Erreichen des jeweiligen Schwellenwerts (für Dienstleistungen id. R. ab 221.000 € netto, *Stand/Schwellenwert-Rhythmus regelmäßig prüfen*) veröffentlichen.
3. **DTVP – Deutsches Vergabeportal ([dtvp.de](https://www.dtvp.de))**
   * *Fokus:* Bundesweite Plattform für Kommunen, Landesbehörden und Zweckverbände.
   * *Bedeutung:* Sehr hohe Relevanz für Vergaben unterhalb der EU-Schwellenwerte (z. B. kommunale Digitalprojekte).
4. **Vergabeportal der Bundesländer (z. B. [vergabe.bayern.de](https://www.vergabe.bayern.de) / [vergabe.hessen.de](https://vergabe.hessen.de))**
   * *Fokus:* Landesspezifische Plattformen der jeweiligen Ministerien, Landesoberbehörden und Landesbetriebe IT.
   * *Bedeutung:* Viele Bundesländer bündeln dort auch kommunale Bedarfe; ideal für regionale Einstiegsprojekte.
5. **Deutsches Ausschreibungsblatt ([deutsches-ausschreibungsblatt.de](https://www.deutsches-ausschreibungsblatt.de))**
   * *Fokus:* Einer der führenden privaten Aggregatoren und Publikationsorgane für Bund, Länder und Kommunen.
   * *Bedeutung:* Umfassender Marktüberblick für Dienstleistungen und Lieferungen mit guten Filteroptionen.

---

## 2. Drei realistische Auftragsarten für eine KI-KMU (Jarvis GmbH)

### A. Machbarkeitsstudien & Proof-of-Concepts (PoC) zur KI-Einführung
* **Typischer Titel:** *„Erstellung einer Machbarkeitsstudie und prototypische Erprobung generativer KI in der Sachbearbeitung“*
* **Warum gewinnbar?**
  * Behörden scheuen das Risiko von Großausschreibungen bei neuen Technologien und vergeben vorgeschaltete Studien oft in Losen oder freihändigen Vergaben / Verhandlungsvergaben unter Schwellenwert.
  * Agilität, wissenschaftliche Methodik und Technologieverständnis stechen hier Großkonzerne aus, die für solche Kleinaufträge (20.000 – 60.000 €) oft zu hohe Tagessätze haben.

### B. DSGVO-konformes Wissensmanagement / RAG-Chatbot für interne Fachdaten
* **Typischer Titel:** *„Konzeption und Bereitstellung eines internen KI-Assistenzsystems auf Basis behördlicher Leitfäden und Gesetzestexte“*
* **Warum gewinnbar?**
  * Behörden benötigen Retrieval-Augmented Generation (RAG) mit strikter Datenhoheit (On-Premise oder Bundes-Cloud/deutsche Rechenzentren).
  * Große Standard-SaaS-Tools scheiden oft aus Datenschutzgründen aus. Eine spezialisierte KI-Boutique kann mit maßgeschneiderter Open-Source-LLM-Infrastruktur (z. B. Mistral/Llama lokal gehostet) punkten.

### C. Automatisierte Dokumentenklassifikation & Informationsextraktion (OCR + NLP)
* **Typischer Titel:** *„Entwicklung einer Schnittstelle zur semantischen Analyse und Vorverarbeitung von Bürgeranträgen / Posteingängen“*
* **Warum gewinnbar?**
  * Klare Problemstellung, messbare Metriken (Präzision/Recall).
  * Häufig als Innovationsausschreibung oder Teilprojekt im Rahmen des OZG (Onlinezugangsgesetz) formuliert, bei denen Fach-Know-how in Machine Learning gegenüber reinen IT-Systemhäusern den Ausschlag gibt.

---

## 3. Angebots-Skizze (Fiktiver Auftrag)

**Ausschreibungstitel:** *„Pilotprojekt: RAG-basierter KI-Fachassistent für den kommunalen Bürgerservice“*  
**Auftraggeber:** *Fiktive Stadtverwaltung Musterstadt (Kämmerei / Digitalisierungsreferat)*

### 1. Verständnis der Aufgabenstellung
Die Stadt Musterstadt beabsichtigt, Sachbearbeiter bei komplexen Bürgeranfragen zu entlasten. Es existiert eine heterogene Wissensbasis (PDFs, Verwaltungsvorschriften, Satzungen).  
*Herausforderung:* Die Auskünfte müssen rechtskonform, quellenbelegt und vollständig datenschutzkonform (DSGVO, Speicherung in DE/EU, kein Training auf sensiblen Daten) generiert werden. Die Jarvis GmbH hat verstanden, dass hier primär Halluzinationssicherheit und Benutzerakzeptanz im Vordergrund stehen.

### 2. Lösungskonzept
* **Architektur:** Implementierung einer RAG-Pipeline (Vektordatenbank + semantische Suche) kombiniert mit einem Open-Source-LLM, gehostet auf souveräner deutscher Cloud-Infrastruktur (z. B. STACKIT oder Open Telekom Cloud) oder kommunaler Server-Infrastruktur.
* **Sicherheit:** Rollen- und Rechtemanagement, Prompt-Injection-Schutz, zwingende Quellenangabe (Zitate mit Verlinkung auf das Primärdokument).
* **Vorgehen:** 
  1. Extraktion und Chunking der Satzungen/Dienstanweisungen.
  2. Prototypische Anbindung an ein Web-GUI für Sachbearbeiter.
  3. Evaluierung mittels „Human-in-the-Loop“-Feedbackschleife.

### 3. Zeitplan (Gesamtdauer: 12 Wochen)
* **Woche 1–2 (Setup & Anforderungsanalyse):** Bereitstellung der Infrastruktur, Definition der Testdaten und Qualitätsmetriken.
* **Woche 3–6 (Entwicklung MVP):** Aufbau der RAG-Pipeline, Parsing der Dokumente, Initiales Prompt-Engineering.
* **Woche 7–9 (Pilotbetrieb / Testphase):** Bereitstellung für 10 Test-Sachbearbeiter, Messung von Treffergenauigkeit und Halluzinationsrate.
* **Woche 10–12 (Feinschliff & Abschlussbericht):** Performance-Optimierung, Schulung der Key-User, Übergabe der Dokumentation und Betriebsunterlagen.

### 4. Preisrahmen (Kalkulationsentwurf)
* **Phase 1: Setup & Konzeption:** 8 PT à 1.150 € = 9.200 €
* **Phase 2: RAG-Implementierung & Integration:** 20 PT à 1.150 € = 23.000 €
* **Phase 3: Testing, Evaluation & Anpassungen:** 10 PT à 1.150 € = 11.500 €
* **Phase 4: Schulung, Doku & Projektabschluss:** 5 PT à 1.150 € = 5.750 €
* **Gesamtbudget-Entwurf:** **49.450 € netto** *(zzgl. Infrastruktur-/Hostingkosten nach Beleg)*

---

## 4. Checkliste: Registrierungsvoraussetzungen für eine GmbH auf Vergabeportalen

Um für öffentliche Ausschreibungen sofort bieterfähig zu sein, muss die Jarvis GmbH folgende Unterlagen und Voraussetzungen vorab vorbereiten:

### A. Rechtliche & Unternehmensnachweise
- [ ] **Handelsregisterauszug (HRB):** Aktuell (nicht älter als 3 bis 6 Monate).
- [ ] **Gewerbeanmeldung / Gewerbeummeldung:** Kopie der Bestätigung.
- [ ] **Steuerliche Unbedenklichkeitsbescheinigung:** Ausgestellt durch das zuständige Finanzamt.
- [ ] **Unbedenklichkeitsbescheinigung der Berufsgenossenschaft:** Nachweis der Beitragszahlung (z. B. BG ETEM / VBG).
- [ ] **Unbedenklichkeitsbescheinigungen der Krankenkassen:** Von den Krankenkassen, bei denen die meisten Mitarbeiter gemeldet sind (Beitragsnachweis).

### B. Technische & Authentifizierungs-Voraussetzungen
- [ ] **Qualifizierte elektronische Signatur (qeS) oder Unternehmenskonto (ELSTER):** 
  * Viele Portale verlangen für elektronische Angebote (Bietertools) eine Signaturkarte / Softwarezertifikat (z. B. D-Trust, governikus) bzw. den Login via ELSTER-Unternehmenskonto.
- [ ] **Installation spezifischer Bietertools:** (z. B. *AI-Bietercockpit* für e-Vergabe oder *subreport ELViS Client*).

### C. Standard-Erklärungen & Versicherungsschutz
- [ ] **Eigenerklärung zur Zuverlässigkeit (§§ 123, 124 GWB):** Bestätigung, dass keine Insolvenz, schwere Verfehlungen oder Schwarzarbeit vorliegen.
- [ ] **Mindestlohnerklärung / Tariftreueerklärung:** Je nach Bundesland verpflichtend.
- [ ] **Betriebs- & IT-Haftpflichtversicherung:** Deckungszusage/Police mit ausreichender Deckungssumme (typischerweise mind. 2–3 Mio. € für Personen-/Sachschäden, mind. 500.000 € bis 1 Mio. € für reine Vermögens-/IT-Schäden).
- [ ] **DSGVO-Verpflichtung & Auftragsverarbeitungs-Muster (AVV):** Bestätigung der Konformität.

### D. Optional, aber stark empfohlen
- [ ] **Präqualifikation (PQ-VOL / AVPQ):** Eintragung in das amtliche Verzeichnis präqualifizierter Unternehmen (reduziert den Nachweisaufwand bei jeder einzelnen Vergabe erheblich).
