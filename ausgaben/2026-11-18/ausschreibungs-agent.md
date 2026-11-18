# Arbeitsprobe: ausschreibungs-agent

# Arbeitsprobe: Ausschreibungs-Recherche und Angebotsentwurf
**Erstellt von:** Ausschreibungs-Agent, Jarvis GmbH  
**Status:** Interner Entwurf / Vorbereitung (Es werden keine Angebote eigenständig eingereicht)

---

## 1. Typische Vergabeportale in Deutschland

Für öffentliche Ausschreibungen auf Bundes-, Länder- und Kommunalebene sind insbesondere folgende Plattformen relevant:

1. **e-Vergabe des Bundes (`evergabe-online.de`)**  
   * **Fokus:** Zentrale Vergabeplattform der Bundesverwaltung (z. B. Beschaffungsamt des BMI, Bundeswehr, Bundesministerien).  
   * **Relevanz:** Primäre Anlaufstelle für überregionale und bundesweite IT-Projekte.
2. **Deutsches Vergabeportal (`dtvp.de`)**  
   * **Fokus:** Weit verbreitete Plattform für Bundes-, Landes- und insbesondere Kommunalverwaltungen.  
   * **Relevanz:** Hohe Dichte an IT- und Digitalisierungsprojekten auf Stadt- und Landkreisebene.
3. **service.bund.de**  
   * **Fokus:** Aggregator für Ausschreibungen, Stellen und Bekanntmachungen des Bundes und nachgeordneter Behörden.  
   * **Relevanz:** Gute Metasuche zum Monitoring von Bekanntmachungen vor dem Wechsel auf die spezifische Vergabeplattform.
4. **TED (Tenders Electronic Daily – `ted.europa.eu`)**  
   * **Fokus:** Amtsblatt der EU für Ausschreibungen oberhalb der EU-Schwellenwerte (für Dienstleistungen derzeit ab 221.000 € bzw. 143.000 € je nach Auftraggebertyp; *Stand: 2024, Schwellenwerte turnusmäßig prüfen*).  
   * **Relevanz:** Wichtig für Konsortial- oder Unteraufträge bei Großprojekten.
5. **Länder-Vergabeportale (z. B. Vergabeplattform Hessen / Bayern / Berlin)**  
   * **Fokus:** Bundeslandspezifische Portale (z. B. `vergabe.hessen.de`, `auftraege.bayern.de`).  
   * **Relevanz:** Oft geringere Schwellenwerte und vereinfachte Verfahren (z. B. Verhandlungsvergaben ohne Teilnahmewettbewerb) für regionale Digitalisierungsinitiativen.

---

## 2. Drei realistische Auftragsarten für eine kleine KI-GmbH

| Auftragsart | Typischer Umfang / Verfahren | Begründung (Warum gewinnbar?) |
| :--- | :--- | :--- |
| **1. Machbarkeitsstudien & PoC-Entwicklungen (Proof of Concept)** | Oft Unterschwellenvergabe / Verhandlungsvergabe (Wert: 25.000 – 80.000 €) | Behörden wollen KI erproben, ohne Großaufträge zu vergeben. Große Systemhäuser bieten hier oft zu starre, teure Pauschalen. Eine kleine GmbH überzeugt mit Agilität, Schnelligkeit und fokussierter Expertise. |
| **2. Interne Wissens- und Chatbots (RAG-Systeme für Behördenakten)** | Beschränkte Ausschreibungen oder Verhandlungsvergaben (Wert: 40.000 – 120.000 €) | Hohe Nachfrage zur Bewältigung von Personalmangel. Behörden fordern meist On-Premise- oder souveräne Cloud-Lösungen (DSGVO-konform). Spezialisierte Start-ups/KMUs haben hier oft modernere Open-Source-LLM-Stacks als Altsystemanbieter. |
| **3. Schulungen, Prompt-Engineering & KI-Readiness-Assessments** | Direktaufträge oder vereinfachte Leistungsbeschreibungen (Wert: 10.000 – 40.000 €) | Geringe formale Hürden bezüglich Bilanzsummen oder Mitarbeiteranzahl. Vergabe erfolgt primär über Personenzertifikate, methodisches Vorgehen und didaktische Qualität. |

---

## 3. Fiktive Angebots-Skizze

**Auftrag:** *„Konzeption und Bereitstellung eines datenschutzkonformen KI-Suchassistenten (RAG) für das interne Rats- und Bürgerinformationssystem der Stadtverwaltung Musterstadt“*

### 3.1. Verständnis der Aufgabenstellung
Die Stadtverwaltung Musterstadt verfügt über umfangreiche Bestände an Beschlussvorlagen, Sitzungsprotokollen und Satzungen. Mitarbeiter und Gremienmitglieder verbringen signifikante Arbeitszeit mit manueller Recherche. Ziel ist ein internes Assistenzsystem auf Basis eines Retrieval-Augmented-Generation-Ansatzes (RAG), das verlässliche Antworten liefert, Quellen präzise referenziert und vollständig im datenschutzrechtlich sicheren Raum (lokal/souveräne Cloud) betrieben wird.

### 3.2. Lösungskonzept (Technischer Ansatz)
* **Architektur:** Open-Source-LLM (z. B. Llama-3- oder Mistral-Derivat) gehostet auf souveräner deutscher Cloud-Infrastruktur oder dedizierter behördlicher Hardware (DSGVO-konform, kein Drittland-Datentransfer).
* **Pipeline:** Dokumentenaufbereitung (PDF, DOCX) inkl. OCR, Einbettung via Embedding-Modell, Speicherung in Vektordatenbank (z. B. Qdrant / PostgreSQL mit pgvector).
* **Sicherheit & Nachvollziehbarkeit:** Strikte Quellenzitierung (Deep-Links auf Absätze), rollenbasierte Zugriffskontrolle (RBAC) und Filter gegen Halluzinationen.

### 3.3. Zeit- und Meilensteinplan
* **Woche 1–2 (M1):** Anforderungsanalyse, Dateninventur, Sicherheitskonzept & DSGVO-Prüfung.
* **Woche 3–5 (M2):** Aufbau der RAG-Pipeline, Indexierung Testdatenbestand, Minimal Viable Product (MVP).
* **Woche 6–7 (M3):** Evaluation (Recall/Precision), Prompt-Optimierung, Anbindung an Benutzeroberfläche.
* **Woche 8 (M4):** Pilotbetrieb, Mitarbeiterschulung (2 Workshops) und Projektabnahme.

### 3.4. Preisrahmen (Indikative Skizze)
* **Phase 1: Konzeption & Setup:** 8.500 €
* **Phase 2: RAG-Entwicklung & Integration:** 24.000 €
* **Phase 3: QA, Test & Schulung:** 6.500 €
* **Gesamtpreis (Dienstleistung):** **39.000 € zzgl. USt.**  
*(Laufende Infrastruktur- und Wartungskosten optional via Service-Level-Agreement: ca. 1.200 € / Monat).*

---

## 4. Checkliste: Was benötigt eine GmbH für die Portal-Registrierung?

Bevor Angebote eingereicht werden können, müssen die formalen Registrierungshürden genommen werden:

### A. Unternehmensdaten & Stammdaten
- [ ] Vollständiger Firmenname, Rechtsform, Sitz laut Handelsregister
- [ ] Handelsregisterauszug (HRB, meist nicht älter als 3–6 Monate)
- [ ] Umsatzsteuer-Identifikationsnummer (USt-IdNr.) und Steuernummer
- [ ] Angabe der wirtschaftlich Berechtigten (Transparenzregister)

### B. Digitale Authentifizierung & Signaturen
- [ ] **Unternehmenskonto / ELSTER-Zertifikat:** Zur eindeutigen behördlichen Authentifizierung („Mein Unternehmenskonto“).
- [ ] **Fortgeschrittene oder qualifizierte elektronische Signatur (qeS):** Je nach Vergabeverfahren und Portal erforderlich, um Angebote rechtsverbindlich zu unterzeichnen (z. B. via Signaturkarte oder Fernsignaturdienst).

### C. Eignungsnachweise und Eigenerklärungen (Standard-Vorbereitung)
- [ ] **Eigenerklärung zu Ausschlussgründen:** Bestätigung nach §§ 123, 124 GWB (keine schweren Verfehlungen, keine Insolvenz, Zahlung von Steuern/Abgaben).
- [ ] **Unbedenklichkeitsbescheinigungen:**
  - Finanzamt
  - Krankenkassen (Krankenkasse mit den meisten Beschäftigten)
  - Berufsgenossenschaft
- [ ] **Gewerbeanmeldung** bzw. Gewerbezentralregisterauszug
- [ ] **Betriebshaftpflichtversicherung:** Nachweis über Deckungssummen für Vermögens- und Personenschäden.

### D. Technisches Bieterprofil
- [ ] Hinterlegung relevanter **CPV-Codes** (Common Procurement Vocabulary), z. B.:
  - `72000000-5` (IT-Dienste: Beratung, Software-Entwicklung, Internet und Hilfestellung)
  - `72212000-4` (Entwicklung von Anwendungssoftware)
  - `73000000-2` (Forschungs- und Entwicklungsdienste)
- [ ] Benennung von vertretungsberechtigten Nutzern und Rollen im jeweiligen Portal.
