# Arbeitsprobe: ausschreibungs-agent

# Ausschreibungs-Recherche & Angebots-Skizze
**Erstellt von:** Ausschreibungs-Agent, Jarvis GmbH  
**Status:** Interner Arbeitsentwurf (Keine verbindliche Abgabe)  
**Datum:** [Aktueller Tag]

---

### Hinweis zur Rolle
Dieser Bericht dient ausschließlich der internen Sondierung, Recherche und methodischen Vorbereitung für die Geschäftsführung der Jarvis GmbH. Es werden im Rahmen dieser Arbeitsschritte **keine** verbindlichen Angebote eingereicht oder Erklärungen gegenüber Vergabestellen abgegeben.

---

## 1. Top-5 Vergabeportale in Deutschland

Für IT- und KI-Dienstleistungen relevanter Bundes-, Landes- und Kommunalaufträge sind folgende Plattformen zentral:

1. **e-Vergabe des Bundes (evergabe-online.de)**  
   *Fokus:* Bundeseinrichtungen, Ministerien, Bundesämter (z. B. Beschaffungsamt des BMI).  
   *Bedeutung:* Das wichtigste Portal für nationale und EU-weite Vergaben auf Bundesebene.
2. **Deutsches Vergabeportal (DTVP – dtvp.de)**  
   *Fokus:* Länder, Landkreise, Städte und Kommunen sowie nachgeordnete Behörden.  
   *Bedeutung:* Sehr hohe Dichte an mittelständischen und kleineren IT-Ausschreibungen; intuitive Bieter-Oberfläche.
3. **Vergabe24 / Staatsanzeiger (vergabe24.de)**  
   *Fokus:* Regionale Vergaben (insb. Baden-Württemberg, Bayern, Hessen, Thüringen, Sachsen u. a.).  
   *Bedeutung:* Stark im kommunalen Bereich und bei Stadtwerken/regionalen Körperschaften.
4. **TED – Tenders Electronic Daily (ted.europa.eu)**  
   *Fokus:* EU-weite Bekanntmachungen oberhalb der EU-Schwellenwerte (auch alle deutschen Oberschwellenvergaben).  
   *Bedeutung:* Pflicht für strategische Marktbeobachtung größerer Rahmenverträge.
5. **subreport ELViS (subreport.de)**  
   *Fokus:* Kommunale Träger, öffentliche Versorger und privatwirtschaftlich regulierte Auftraggeber.  
   *Bedeutung:* Häufig genutzt für spezialisierte Fachverfahren und Pilotprojekte im kommunalen Sektor.

---

## 2. Drei gewinnbare Auftragsarten für eine kleine KI-GmbH

Für die Jarvis GmbH eignen sich Aufträge, bei denen Agilität, methodisches Spezialwissen und DSGVO-Konformität Vorrang vor reiner Personalkapazität haben:

### A. Machbarkeitsstudien & Proof-of-Concepts (PoC) zur Prozessautomatisierung
* **Beispiel:** „Erstellung einer Machbarkeitsstudie zum Einsatz von KI-Sprachmodellen zur automatisierten Bearbeitung von Bürgeranfragen im Posteingang.“
* **Begründung:** Häufig als Verhandlungsvergabe oder beschränkte Ausschreibung unterhalb des EU-Schwellenwerts (Unterschwellenvergabe) vergeben. Große Systemhäuser bieten hier oft standardisierte, überdimensionierte Lösungen an. Eine kleine GmbH punktet mit Schnelligkeit, Unabhängigkeit bei der Modellauswahl (z. B. Open-Source vs. Hosted) und kosteneffizienter Umsetzung.

### B. Entwicklung maßgeschneiderter Retrieval-Augmented-Generation-(RAG)-Systeme für Fachdatenbanken
* **Beispiel:** „Entwicklung einer internen semantischen Wissenssuche für juristische Dokumente/Bauamtsakten auf Basis lokaler LLMs.“
* **Begründung:** Behörden verlangen zwingend DSGVO-Konformität und oft On-Premise- bzw. souveräne Cloud-Lösungen. Kleine, hochspezialisierte Teams können Open-Source-Pipelines (z. B. Llama-3/Mistral via lokaler Infrastruktur) maßschneidern, ohne teure Enterprise-Lizenzen Dritter aufzuzwingen.

### C. KI-Readiness-Assessments, Prompt-Engineering- & Governance-Workshops
* **Beispiel:** „Konzeption und Durchführung von Qualifizierungsmaßnahmen zum sicheren Einsatz generativer KI im Verwaltungsalltag.“
* **Begründung:** Reines Dienstleistungsmandat ohne hohes Implementierungs- oder Gewährleistungsrisiko. Eignet sich ideal zum Aufbau von Behörden-Referenzen und führt häufig zu Folgeaufträgen in der technischen Umsetzung.

---

## 3. Angebots-Skizze (Fiktiver Auftrag)

* **Auftragstitel:** *„Pilotprojekt: KI-gestützte Extraktion und semantische Verschlagwortung von Stadtratsbeschlüssen für das Dokumentenmanagementsystem (DMS) der Stadt Musterhausen“*
* **Verfahren:** Verhandlungsvergabe ohne Teilnahmewettbewerb (Unterschwelle)

### 3.1. Verständnis der Aufgabenstellung
Die Stadt Musterhausen verfügt über einen umfangreichen Bestand unstrukturierter PDF-Beschlussvorlagen. Die manuelle Verschlagwortung bindet wertvolle Fachressourcen und führt zu uneinheitlichen Metadaten.  
Ziel ist die Bereitstellung einer automatisierten Pipeline, die relevante Entitäten (Zuständigkeiten, Fristen, Finanzvolumina, Schlagworte) fehlerarm extrahiert und DSGVO-konform an das bestehende DMS übergibt.

### 3.2. Lösungskonzept
1. **Architektur:** Implementierung einer Container-basierten RAG-/Extraktions-Pipeline (Docker/Kubernetes) im Rechenzentrum des Auftraggebers oder in einer BSI-zertifizierten deutschen Cloud.
2. **Modellauswahl:** Einsatz modernster Open-Source-Sprachmodelle, fine-tuned auf deutsches Verwaltungsvokabular. Keine Datenübertragung an Server außerhalb der EU.
3. **Integration:** Bereitstellung einer standardisierten REST-API zur Übergabe strukturierter JSON-Metadaten an das DMS.
4. **Qualitätssicherung:** „Human-in-the-Loop“-Dashboard für Sachbearbeiter zur Freigabe/Korrektur mit integrierter Feedbackschleife (Aktives Lernen).

### 3.3. Zeit- und Projektplan (Gesamtlaufzeit: 10 Wochen)
* **Woche 1–2 (Phase 1):** Kick-Off, Anforderungsfeinspezifikation, Bereitstellung & Analyse der Beispieldaten.
* **Woche 3–5 (Phase 2):** Aufbau der Pipeline, Modell-Feinschliff und Entwicklung der Parsing-Logik.
* **Woche 6–7 (Phase 3):** Anbindung an das Test-DMS, Validierung anhand eines Testdatensatzes (Target: >90 % F1-Score bei Kernentitäten).
* **Woche 8–9 (Phase 4):** Pilotbetrieb, Schulung der Schlüsselanwender (Key-User).
* **Woche 10 (Phase 5):** Abschlussbericht, Übergabe der Dokumentation und Betriebsunterlagen.

### 3.4. Preisrahmen (Kalkulationsbeispiel)
* **Festpreis-Paket (Pilotphase):**
  * Phase 1 & 2 (Setup & Modellpipeline): 16 PT à 1.150 € = 18.400 €
  * Phase 3 (DMS-Integration & Testing): 10 PT à 1.150 € = 11.500 €
  * Phase 4 & 5 (Pilotierung, Schulung, Doku): 6 PT à 1.150 € = 6.900 €
* **Gesamtbudget:** **36.800,00 € netto** *(zzgl. USt.)*  
*(Optionaler Wartungsvertrag nach Pilotphase: 850,00 €/Monat)*

---

## 4. Checkliste: Was braucht die Jarvis GmbH zur Registrierung & Bieterqualifikation?

Um auf Vergabeportalen registriert und angebotsfähig zu sein, müssen vorab folgende Dokumente und Werkzeuge vorliegen:

### A. Technische & Administrative Voraussetzungen
- [ ] **ELSTER-Unternehmenskonto / Bieter-Zertifikat:** Viele Portale setzen ein Organisationskonto via ELSTER für den Identitätsnachweis voraus.
- [ ] **Elektronische Signatur:** Mindestens fortgeschrittene elektronische Signatur (FES), für viele EU-Vergaben qualifizierte elektronische Signatur (QES) für die Geschäftsführung.
- [ ] **Zentrale Registrierungen:** 
  - Registrierung im Amtlichen Verzeichnis präqualifizierter Unternehmen (AVPQ) der IHK (optional, reduziert aber den Nachweisaufwand massiv).
  - Anlegen von Bieterprofilen auf *evergabe-online.de* und *DTVP*.

### B. Standard-Eignungsnachweise (Formalia, max. 3–6 Monate alt vorhalten)
- [ ] **Handelsregisterauszug (HRB):** Aktueller Registerauszug.
- [ ] **Gewerbeanmeldung / -ummeldung.**
- [ ] **Steuerliche Unbedenklichkeitsbescheinigung:** Vom zuständigen Finanzamt.
- [ ] **Unbedenklichkeitsbescheinigungen der Sozialversicherungsträger:** Von den Krankenkassen der Mitarbeiter sowie der Berufsgenossenschaft (z. B. VBG).
- [ ] **Nachweis der Betriebshaftpflicht- & Vermögensschadenhaftpflicht:** Deckungssummen (üblich: mind. 1–2 Mio. € für Personenschäden, mind. 500k–1 Mio. € für Vermögens-/IT-Schäden).

### C. Standardisierte Eigenerklärungen (Vorlagen bereithalten)
- [ ] Erklärung zum Nichtvorliegen von Ausschlussgründen gem. §§ 123, 124 GWB (Strafregister, Insolvenz, schwere Verfehlungen).
- [ ] Eigenerklärung zur Einhaltung des Mindestlohngesetzes (MiLoG) und landesspezifischer Tariftreuegesetze.
- [ ] Erklärung zu Russland-Sanktionen (Verordnung (EU) Nr. 833/2014 Art. 5k).
- [ ] DSGVO-Compliance-Nachweis / Technisch-Organisatorische Maßnahmen (TOM-Konzept).

### D. Fachliche Unterlagen
- [ ] **Referenzliste:** Mindestens 2–3 anonymisierte oder freigegebene Case Studies über erfolgreich durchgeführte Data-Science- / KI-Projekte.
- [ ] **Qualifikationsprofile:** Standardisierte CVs der Kernmitarbeiter inkl. Zertifikate (Scrum, Cloud-Zertifizierungen, Studienabschlüsse).
