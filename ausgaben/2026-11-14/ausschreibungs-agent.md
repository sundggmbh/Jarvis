# Arbeitsprobe: ausschreibungs-agent

# Jarvis GmbH – Arbeitsprobe: Recherche & Konzeption Öffentliche Ausschreibungen (KI-Dienstleistungen)

**Rolle:** Ausschreibungs-Agent der Jarvis GmbH  
**Status:** Interner Entwurf / Nur Recherche und Skizzierung (Keine verbindliche Angebotsabgabe)  
**Hinweis zur Aktualität:** Angaben zu Schwellenwerten, Vergabeplattform-Schnittstellen und Formblättern basieren auf dem Wissensstand bis Anfang 2024. Spezifische Plattformprozesse (z. B. Umstellung auf BundID/ELSTER) können sich dynamisch ändern und sind vor finaler Nutzung fallweise zu verifizieren.

---

## 1. Fünf typische Portale für öffentliche Ausschreibungen in Deutschland

| Portal | Ebene / Träger | Relevanz & Einsatzbereich |
| :--- | :--- | :--- |
| **1. e-Vergabe des Bundes** (`evergabe-online.de` / `service.bund.de`) | Bund / Bundesbehörden | Zentrale Plattform für Beschaffungen ober- und unterhalb der EU-Schwellenwerte für Bundesministerien, Bundesämter und Institute. |
| **2. TED (Tenders Electronic Daily)** (`ted.europa.eu`) | EU-weit (inkl. Bund/Länder) | Pflichtveröffentlichung für alle Vergaben oberhalb der EU-Schwellenwerte (z. B. Liefer- und Dienstleistungen ab ca. 215.000 € bzw. 140.000 € für oberste Bundesbehörden). |
| **3. Vergabemarktplatz NRW** (`vergabe.nrw.de`) | Land & Kommunen (NRW) | Repräsentativ für Landesportale (Teil der d-NRW-Infrastruktur); bündelt Ausschreibungen von Landesministerien, Bezirksregierungen und zahlreichen Städten/Kreisen. |
| **4. HAD – Hessische Ausschreibungsdatenbank** (`had.de`) / **Aufträge Bayern** (`auftraege.bayern.de`) | Bundesländer / Kommunen | Typische Portale zur Abdeckung regionaler Ausschreibungen unterhalb der EU-Schwellenwerte in den jeweiligen Bundesländern. |
| **5. Deutsches Ausschreibungsblatt / Vergabe24** | Bundesweiter Aggregator | Kommerzielle Plattformen, die Ausschreibungen von Bund, Ländern und tausenden Einzelkommunen aggregieren; ideal für das Screening kleinerer Freihändiger Vergaben / Verhandlungsvergaben. |

---

## 2. Drei realistische Auftragsarten für eine kleine KI-GmbH

Für eine kleine GmbH (unter 10–20 Mitarbeitende) sind Megaprojekte mit 7-stelligen Budgets oft aufgrund harter Eignungskriterien (z. B. Umsatzanforderungen, Mindestanzahl ähnlicher Referenzen) nicht erreichbar. Folgende drei Auftragsarten bieten die höchsten Zuschlagswahrscheinlichkeiten:

### Auftragsart A: Machbarkeitsstudien & Proof of Concept (PoC)
* **Beispiel:** „Machbarkeitsanalyse und Erstellung eines Prototyps zur automatisierten Textzusammenfassung von Ratsdrucksachen.“
* **Typisches Verfahren:** Verhandlungsvergabe ohne Teilnahmewettbewerb oder beschränkte Ausschreibung im Unterschwellenbereich (Volumen ca. 25.000 – 80.000 €).
* **Begründung für Gewinnchancen:** 
  * Der Fokus liegt auf Agilität, Technologiekompetenz und Innovationsgrad, nicht auf Firmenhistorie oder Konzernstrukturen.
  * Öffentliche Auftraggeber suchen hier oft explizit nach praxisnahen KI-Spezialisten, um Digitalisierungsbudgets risikolos zu erproben.

### Auftragsart B: Implementierung von Fach-RAG-Systemen & Semantischer Suche
* **Beispiel:** „Einführung eines DSGVO-konformen semantischen Assistenzsystems (RAG) auf internen Aktenbeständen für eine Landesbehörde.“
* **Typisches Verfahren:** Öffentliche Ausschreibung oder Direktauftrag nach Markterkundung (Volumen ca. 60.000 – 150.000 €).
* **Begründung für Gewinnchancen:** 
  * Hoher Bedarf: Behörden dürfen aus Datenschutzgründen keine offenen Consumer-LLMs nutzen, benötigen aber Entlastung bei der Dokumentenrecherche.
  * Spezialisierung: Eine kleine GmbH kann durch den Einsatz von Open-Source-Modellen (z. B. Llama/Mistral) im BSI-konformen On-Premise- oder GovCloud-Betrieb punkten, wo Standard-Systemhäuser oft zu starr sind.

### Auftragsart C: Prompt-Engineering- & KI-Befähigungsschulungen
* **Beispiel:** „Konzeption und Durchführung von Praxis-Workshops zum Einsatz generativer KI im behördlichen Arbeitsalltag inkl. Leitfadenerstellung.“
* **Typisches Verfahren:** Freihändige Vergabe / Verhandlungsvergabe (Volumen ca. 10.000 – 40.000 €).
* **Begründung für Gewinnchancen:**
  * Extrem geringe bürokratische Hürden; Zuschlag erfolgt primär nach Beraterprofilen/CVs der Dozenten und didaktischem Konzept.
  * Geringes finanzielles Risiko und strategischer Einstieg, um Folgeprojekte bei der Behörde zu platzieren.

---

## 3. Angebots-Skizze (Fiktiver Auftrag)

* **Auftraggeber:** Digitalisierungsamt der Modellstadt Neustadt
* **Projekt:** *„Pilotprojekt: KI-gestützte Vorprüfung und Klassifikation von Bürgeranträgen im PDF-Format“*

### 3.1 Verständnis der Ausgangslage & Zielsetzung
Die Stadt Neustadt verzeichnet steigende Fallzahlen bei der Bearbeitung formloser Bürgeranträge per PDF/Scan. Die manuelle Zuordnung an Fachämter bindet erhebliche Ressourcen.
* **Ziel:** Entwicklung einer automatisierten Pipeline, die Dokumente klassifiziert, Pflichtangaben (Name, Aktenzeichen, Anliegen) extrahiert und ein Routing-Signal für das bestehende DMS liefert.
* **Kritische Faktoren:** 100 % DSGVO-Konformität, kein Abfluss von Bürgerdaten in US-Cloud-Infrastrukturen, transparente Fehlertoleranz (Human-in-the-Loop-Prinzip).

### 3.2 Lösungskonzept (Technologie & Vorgehen)
1. **Architektur:** 
   * Lokales OCR-Preprocessing (z. B. Tesseract / Surya).
   * Selbst gehostetes, quelloffenes LLM / Extraktionsmodell (Deployment auf bestehenden kommunalen Servern oder zertifiziertem deutschem Rechenzentrum).
2. **Datenschutz & Sicherheit:**
   * Anonymisierungs- und Pseudonymisierungsmodul vor der Modellverarbeitung.
   * Keine Speicherung von Trainingsdaten während des Inferenzbetriebs.
3. **Integration & Schnittstellen:**
   * Bereitstellung einer leichtgewichtigen REST-API zur Übergabe strukturierter JSON-Daten an das DMS der Stadt.
   * Prüf-Dashboard: Unsichere Klassifikationen (< 85 % Konfidenz) werden gezielt Sachbearbeitern zur Freigabe vorgelegt.

### 3.3 Meilensteine & Zeitplan (Gesamtlaufzeit: 14 Wochen)
* **Phase 1 (Woche 1–3): Anforderungsanalyse & Datenbasis**
  * Definition des Klassifikationsschemas, Übergabe und Bereinigung von anonymisierten Test-Datensätzen.
* **Phase 2 (Woche 4–7): Prototyping & Pipeline-Entwicklung**
  * Aufbau der Extraktions-Pipeline, Prompt-Optimierung / Fine-Tuning und Konfidenz-Scoring.
* **Phase 3 (Woche 8–11): Piloteinsatz & Systemintegration**
  * Anbindung an Testinstanz des DMS, Shadow-Betrieb parallel zur manuellen Prüfung.
* **Phase 4 (Woche 12–14): Evaluierung, Dokumentation & Übergabe**
  * Messung der Extraktionsgenauigkeit, Erstellung Betriebs-/Datenschutzdokumentation, Schulung der Key-User.

### 3.4 Preisrahmen (Festpreis-Kalkulation)

| Leistungsphase | Aufwand (PT) | Tagessatz (netto) | Gesamtpreis (netto) |
| :--- | :--- | :--- | :--- |
| Phase 1: Analyse & Setup | 6 PT | 1.100 € | 6.600 € |
| Phase 2: KI-Pipeline & Modellierung | 16 PT | 1.200 € | 19.200 € |
| Phase 3: Integration & Schnittstellen | 12 PT | 1.100 € | 13.200 € |
| Phase 4: Validierung, Doku & Schulung | 6 PT | 1.000 € | 6.000 € |
| **Projektmanagement & QS (begleitend)** | 5 PT | 1.100 € | 5.500 € |
| **Gesamtsumme (netto):** | **45 PT** | | **50.500 €** |

*(Zzgl. gesetzlicher USt. Keine verdeckten Lizenzkosten durch Fokus auf Open-Source-Komponenten).*

---

## 4. Checkliste: Registrierungs- & Teilnahmevoraussetzungen für die GmbH

Um sich auf Vergabeportalen zu registrieren und Angebote rechtssicher abzugeben, muss eine GmbH folgende Unterlagen und Konten vorbereitet haben:

### A. Technische Zugänge
- [ ] **ELSTER-Unternehmenskonto / Mein Unternehmenskonto (MUK):** Wird zunehmend Standard für den behördlichen Identitätsnachweis.
- [ ] **Signaturkarte / Software-Zertifikat:** Für Vergaben, die eine fortgeschrittene oder qualifizierte elektronische Signatur (qeS) erfordern (bei vielen Vergaben genügt inzwischen Textform nach § 126b BGB, aber nicht bei allen).
- [ ] **Portal-Accounts:** Anlegen der Bieterkonten auf *e-Vergabe des Bundes*, *Vergabe.NRW*, etc.

### B. Rechtliche & administrative Unternehmensdaten
- [ ] **Handelsregisterauszug (aktuell, max. 3–6 Monate alt).**
- [ ] **Gewerbeanmeldung / Gewerbeummeldung.**
- [ ] **Umsatzsteuer-Identifikationsnummer (USt-IdNr.) & Steuernummer.**
- [ ] **Eintragung ins Transparenzregister** (Nachweis wirtschaftlich Berechtigte).

### C. Behördliche Bescheinigungen (Nicht älter als 3 Monate)
- [ ] **Unbedenklichkeitsbescheinigung des Finanzamts** (steuerliche Zuverlässigkeit).
- [ ] **Unbedenklichkeitsbescheinigung der Krankenkassen** (Beiträge zur Sozialversicherung für alle Mitarbeitenden).
- [ ] **Bescheinigung der Berufsgenossenschaft** (BG-Zugehörigkeit und Beitragszahlung).
- [ ] **Gewerbezentralregisterauszug** (GZR, behördlich anzufordern).

### D. Versicherungs- & Bonitätsnachweise
- [ ] **Betriebshaftpflicht- & Vermögensschadenhaftpflicht-Police:** Mit ausreichender Deckung (Standardanforderung: 1–3 Mio. € für Personen-/Sachschäden, mind. 250.000–500.000 € für echte Vermögensschäden).
- [ ] **BWA / Jahresabschlüsse der letzten 1–2 Jahre** (falls Mindestumsätze gefordert sind).

### E. Standard-Eigenerklärungen (Ausschreibungsunterlagen)
- [ ] **Erklärung zum Nichtvorliegen von Ausschlussgründen** gem. §§ 123, 124 GWB (z. B. keine Insolvenz, keine schwere Verfehlung).
- [ ] **Erklärung zur Einhaltung von Mindestlohn- & Tariftreuegesetzen** (länderspezifisch).
- [ ] **Einheitliche Europäische Eigenerklärung (EEE):** XML/PDF-Tool zur standardisierten Eignungsprüfung bei EU-Vergaben.
- [ ] **Referenzliste & CV-Vorlagen:** Formatierte Kurzprofile der KI-Entwickler und 2–3 anonymisierte/freigegebene Projektbeschreibungen vorangegangener Dienstleistungen.
