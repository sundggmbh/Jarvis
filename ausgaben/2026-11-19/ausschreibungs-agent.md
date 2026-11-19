# Arbeitsprobe: ausschreibungs-agent

# Jarvis GmbH – Internes Strategie- & Vorbereitungsdokument
**Rolle:** Ausschreibungs-Agent (Recherche & Konzeption)  
**Status:** Interner Arbeitsentwurf (Keine Angebotsabgabe)

---

## 1. Portale für öffentliche Ausschreibungen in Deutschland

Für Dienstleistungen im Bereich KI und Softwareentwicklung sind folgende 5 Vergabeplattformen zentral:

1. **e-Vergabe des Bundes (`evergabe-online.de` / `bund.de`)**
   * *Fokus:* Zentrale Plattform der Bundesverwaltung (z. B. Bundesministerien, Bundeswehr, Bundesagenturen).
   * *Relevanz:* Große IT-Projekte, aber auch Rahmenverträge und Fach-Consulting.
2. **TED (Tenders Electronic Daily – `ted.europa.eu`)**
   * *Fokus:* EU-weite Ausschreibungen (Vergaben oberhalb der EU-Schwellenwerte).
   * *Relevanz:* Notwendig für größere Vergaben; enthält auch alle Bekanntmachungen deutscher Auftraggeber ab ca. 221.000 EUR (Dienstleistungen, Schwellenwert 2024/2025; *präzise Schwellenwerte vor Bewerbung tagesaktuell prüfen*).
3. **Deutsches Vergabeportal (DTVP – `dtvp.de`)**
   * *Fokus:* Kommunen, Landkreise, Zweckverbände und Landesbehörden.
   * *Relevanz:* Sehr hohe Dichte an praxisnahen, regionalen IT- und Digitalisierungsprojekten.
4. **Vergabemarktplatz NRW (`vergabe.nrw.de`)** *(Exemplarisch für Landesportale, vgl. auch HAD in Hessen oder Vergabe Bayern)*
   * *Fokus:* Landesbehörden, Universitäten und Kommunen eines Bundeslandes.
   * *Relevanz:* Häufig Los-Vergaben oder Pilotprojekte, die für KMU zugänglich sind.
5. **Subreport ELViS (`subreport.de`)**
   * *Fokus:* Privatwirtschaftliche Plattform mit starker Durchdringung im Bereich kommunaler und öffentlicher Auftraggeber.
   * *Relevanz:* Nutzerfreundliche Oberfläche, viele Unterschwellenvergaben.

---

## 2. Drei gewinnbare Auftragsarten für eine kleine KI-GmbH

Kleine Unternehmen (KMU) haben im Bieterwettbewerb gegen IT-Großkonzerne dann die besten Chancen, wenn Spezialwissen, Agilität und Datenschutzkompetenz gefragt sind:

### A. Machbarkeitsstudien & Prototyping (Proof of Concept – PoC)
* **Beispiel:** „Erstellung einer Machbarkeitsstudie zur automatisierten Vorprüfung von Förderanträgen mittels LLMs“.
* **Begründung:** Öffentliche Auftraggeber müssen Risiken minimieren und schreiben vor Millionen-Investitionen oft kleine PoCs aus (oft unterhalb des EU-Schwellenwerts als Verhandlungsvergabe). Eine kleine KI-Agentur kann hier durch Schnelligkeit, moderne Tech-Stacks und maßgeschneiderte Ansätze punkten, ohne seitenlange Großkonzern-Zertifizierungen vorlegen zu müssen.

### B. On-Premises / DSGVO-konforme RAG-Systeme für interne Dokumente
* **Beispiel:** „Einführung eines semantischen Suchassistenten für die Kreisverwaltung auf Basis bestehender Richtlinien und Ratsbeschlüsse“.
* **Begründung:** Datenschutz (DSGVO, BSI-Standards) ist die größte Hürde für Behörden. Eine kleine GmbH, die Open-Source-Modelle (z. B. Mistral, Llama-Derivate) containerisiert auf behördeneigener Infrastruktur oder in sicheren deutschen Clouds aufsetzt, erfüllt genau diese Nische, die Standard-SaaS-Tools (wie ungeschützte US-APIs) nicht bedienen dürfen.

### C. KI-gestützte Datenextraktion & Aktenbereinigung (Digitale Poststelle)
* **Beispiel:** „Klassifizierung und OCR-basierte Informationsextraktion eingehender Fachanträge“.
* **Begründung:** Der Druck durch das Onlinezugangsgesetz (OZG) und den Fachkräftemangel zwingt Kommunen zur Prozessautomatisierung. Das Problem ist klar abgegrenzt, technisch mit Standard-Pipelines lösbar und erfordert keine jahrelange Beratung, sondern greifbare Software-Lieferung.

---

## 3. Angebots-Skizze (Fiktiver Auftrag)

**Ausschreibung (fiktiv):** *„Entwicklung und Pilotierung eines RAG-basierten Wissensassistenten für das Baurechtsamt der Stadt Musterhausen“ (Verhandlungsvergabe ohne Teilnahmewettbewerb / Unterschwelle).*

### 1. Verständnis der Herausforderung
* **Ausgangslage:** Das Baurechtsamt steht vor einem hohen Volumen komplexer Regelwerke (BauGB, LBO, Bebauungspläne). Mitarbeiter verbringen signifikante Zeit mit manueller Textsuche.
* **Ziel:** Ein interner KI-Assistent, der Fragen beantwortet, Quellen präzise referenziert und ausschließlich auf geprüften Dokumenten arbeitet (keine Halluzinationen, kein Abfluss von Daten an Dritte).

### 2. Lösungskonzept
* **Architektur:** Retrieval-Augmented Generation (RAG).
* **Komponenten:**
  * Vektordatenbank (z. B. Qdrant / pgvector) zur Indexierung der PDF- und Word-Bestände.
  * Lokales bzw. souverän gehostetes Sprachmodell (z. B. via Open-Source-LLM auf dedizierter BSI-konformer Cloud-Instanz).
  * Web-Frontend mit Quellennachweis (Zitatsprung direkt ins PDF).
* **Compliance:** 100 % DSGVO-konform, rollenbasiertes Rechtesystem (RBAC), kein Modelltraining mit Behoerdendaten.

### 3. Vorgehens- und Zeitplan (Laufzeit: 12 Wochen)
* **Woche 1–2 (Initialisierung):** Datenübernahme, Schnittstellenprüfung, Anforderungs-Workshop.
* **Woche 3–6 (MVP & Pipeline):** Aufbau der RAG-Pipeline, automatisierte Dokumenten-Ingestion, erste UI-Version.
* **Woche 7–9 (Validierung & Feinjustierung):** Testphase mit 10 Fachanwendern, Prompt Engineering, Evaluation der Antwortgüte (Grounding/Precision).
* **Woche 10–12 (Rollout & Schulung):** Sicherheitsaudit, Übergabe der Dokumentation, 2x Anwenderschulung, Betriebsübergabe.

### 4. Preisrahmen (Indikative Skizze)
* **Paket 1: Setup & Data Ingestion Pipeline:** 14.500 EUR
* **Paket 2: RAG-Entwicklung & UI-Integration:** 22.000 EUR
* **Paket 3: Testing, Dokumentation & Schulung:** 8.500 EUR
* **Gesamtbudget (netto):** **ca. 45.000 EUR** *(Option: Optionaler Wartungsvertrag 1.200 EUR/Monat).*

---

## 4. Checkliste: Was braucht eine GmbH zur Portal-Registrierung & Bieterfähigkeit?

Bevor Angebote eingereicht werden können, müssen folgende Nachweise griffbereit vorliegen (viele Portale verlangen diese bereits beim Registrierungs- bzw. Präqualifizierungsprozess):

### A. Technische & Administrative Basis
- [ ] **Registrierung auf Vergabeplattformen** (Benutzerkonto für Jarvis GmbH anlegen).
- [ ] **ELSTER-Unternehmenskonto** bzw. qualifizierte elektronische Signatur (qeS) / Signaturkarte (viele Portale nutzen für die Authentifizierung das Unternehmenskonto oder fortgeschrittene Signaturen nach eIDAS).
- [ ] **Unternehmensdaten:** Steuernummer, USt-IdNr., DUNS-Nummer (oft bei internationalen/EU-Ausschreibungen gefordert).

### B. Formale & Rechtliche Eignungsnachweise (Standardunterlagen)
- [ ] **Handelsregisterauszug (aktuell):** Nicht älter als 3 bis 6 Monate.
- [ ] **Gewerbeanmeldung / -ummeldung.**
- [ ] **Unbedenklichkeitsbescheinigungen:**
  * Finanzamt (steuerliche Zuverlässigkeit).
  * Krankenkassen (Beitragseinzug der Mitarbeiter).
  * Berufsgenossenschaft (BG).
- [ ] **Eintrag ins Transparenzregister** (Nachweis über wirtschaftlich Berechtigte).
- [ ] **Gewerbezentralregisterauszug** (Beleg, dass keine schweren Verfehlungen vorliegen; kann bei Bedarf behördlich angefordert werden).

### C. Versicherungen & Finanzen
- [ ] **Betriebs- & IT-Haftpflichtversicherung:** Deckungszusage (meist mind. 2–3 Mio. EUR für Personen-/Sachschäden und 500k–1 Mio. EUR für echte Vermögensschäden).
- [ ] **BWA oder Jahresabschlüsse** der letzten 1–3 Jahre (Nachweis der wirtschaftlichen Leistungsfähigkeit).

### D. Fachliche Eignung & Erklärungen (Bieterprofil)
- [ ] **Eigenerklärung zu Ausschlussgründen:** Vordrucke gem. §§ 123, 124 GWB (keine Insolvenz, keine Bestechung, etc.).
- [ ] **Verpflichtungserklärung zum Mindestlohngesetz (MiLoG)** und ggf. Tariftreueerklärungen der Bundesländer.
- [ ] **Referenzliste:** 2 bis 3 vergleichbare Projekte (bei jungen GmbHs: detaillierte CVs/Referenzen der Gründer/Schlüsselpersonen als Projekterfahrung ausweisen).
- [ ] **Datenschutz- und Sicherheitskonzept:** Kurzdarstellung zur Einhaltung von DSGVO und Grundsätzen der IT-Sicherheit (z. B. Anlehnung an ISO 27001 oder BSI IT-Grundschutz).

*(Empfehlung: Hinterlegung des Unternehmens im **Amtlichen Verzeichnis präqualifizierter Unternehmen (AVPQ)** der IHKs, um Standard-Nachweise bundesweit mit einem Zertifikat abkürzen zu können).*
