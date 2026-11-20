# Arbeitsprobe: produkt-agent

# Jarvis GmbH – Produktentwicklung
**Internes Dokument:** Verkaufsvorlage & Produktprobe (B2B Digital Asset)  
**Verfasser:** Produkt-Agent, Jarvis GmbH  
**Status:** Freigegeben zur Monetarisierung  

---

## 1. Titel & Inhaltsverzeichnis des E-Books

### Titel
**Pragmatische KI-Transformation: Der Umsetzungsleitfaden für den deutschen Mittelstand**  
*Untertitel: Wie Inhaber und Geschäftsführer Kernprozesse automatisieren, Fachkräfte entlasten und DSGVO-konform messbaren ROI erzielen – ohne Millionenbudget.*

### Inhaltsverzeichnis
* **Kapitel 1: Der Hype-Filter:** Warum Mittelständler keine Tech-Konzerne kopieren dürfen (und wo der echte Hebel liegt)
* **Kapitel 2: Die Potenzial-Matrix:** Prozesse identifizieren, priorisieren und den harten ROI vor Projektstart berechnen
* **Kapitel 3: DSGVO, Compliance & EU AI Act:** Rechtssicherer Betrieb von KI-Modellen ohne Abfluss von Betriebsgeheimnissen
* **Kapitel 4: Technologie-Stack ohne Vendor-Lock-in:** Wann sich lokale Open-Source-Modelle lohnen und wann Azure/OpenAI Enterprise unverzichtbar sind
* **Kapitel 5: Das Firmen-Gehirn (RAG-Architektur):** Wie Sie unstrukturiertes Unternehmenswissen in Sekunden für Mitarbeiter abrufbar machen
* **Kapitel 6: Der 30-Tage-Pilot:** Schritt-für-Schritt-Implementierung des ersten produktiven Use Cases
* **Kapitel 7: Change Management im Maschinenraum:** Wie Sie Betriebsrat, Belegschaft und Führungskräfte für den Wandel gewinnen
* **Kapitel 8: Skalierung & Governance:** KPIs, Fehlertoleranzen, Monitoring und die Roadmap für das Folgejahr

---

## 2. Muster-Kapitel (Volltext)

### Kapitel 2: Die Potenzial-Matrix – Prozesse identifizieren, priorisieren und den harten ROI vor Projektstart berechnen

Der häufigste Fehler mittelständischer Digitalisierungsinitiativen ist die Jagd nach dem spektakulärsten Anwendungsfall. Viele Unternehmen beginnen mit Prestigeprojekten – etwa einem vollautomatisierten Kundenservice-Avatar oder generativen Design-Experimenten in der F&E. Das Resultat nach sechs Monaten: Budget aufgebraucht, Belegschaft frustriert und die Geschäftsführung zweifelt am generellen Nutzen von Künstlicher Intelligenz.

Pragmatische Transformation beginnt nicht bei dem, was technologisch faszinierend ist, sondern bei dem, was betriebswirtschaftlich schmerzt. Wir nutzen hierfür die **Jarvis-Impact-Matrix**, die Workflows entlang zweier Achsen bewertet: *Standardisierungsgrad* und *Repetitiver Zeitaufwand*.

#### Die drei Kriterien eines rentablen Mittelstands-Use-Cases

Bevor eine einzige Zeile Code geschrieben oder eine Software-Lizenz erworben wird, muss jeder Prozess drei Filter passieren:

1. **Strukturierte Redundanz:** Der Prozess bindet mindestens 15 Personenstunden pro Woche an Tätigkeiten, die auf klaren, wiederkehrenden Regeln basieren (z. B. Angebotsvergleiche von Lieferanten, Klassifizierung eingehender Ausschreibungsunterlagen oder Prüfen von Reklamationsmails).
2. **Vorhandensein von Referenzdaten:** Es existiert ein historischer Datenbestand (Text, Tabellen, PDFs), an dem die Modellgüte objektiv gemessen werden kann.
3. **Fehlertoleranz mit Mensch-im-Loop:** Das System muss nicht zu 100 % autonom agieren. Ein System, das zu 90 % vorverarbeitet und dem Sachbearbeiter lediglich den fertigen Entwurf zur finalen Freigabe vorlegt, eliminiert 70 % der Bearbeitungszeit bei null Prozent Qualitätsverlust.

#### Der Praxis-Case: Angebotsprüfung im technischen Großhandel

Betrachten wir ein typisches mittelständisches Handelshaus mit 120 Mitarbeitern. Bislang trafen täglich rund 40 mehrseitige Leistungsverzeichnisse und Bestellanfragen per PDF ein. Drei Vertriebsinnendienstler verbrachten jeweils zweieinhalb Stunden täglich damit, Artikelnummern, Spezifikationen und Mengengerüste manuell in das ERP-System abzutippen.

* **Zeitaufwand alt:** 3 Mitarbeiter × 2,5 Stunden = 7,5 Stunden/Tag (ca. 150 Stunden/Monat).
* **Vollkosten:** Bei einem durchschnittlichen Stundensatz von 48 Euro entspricht dies **7.200 Euro monatlichen Prozesskosten** für reine Datentypistendienste.

Durch den Einsatz einer lokalen OCR- und RAG-Pipeline (Dokumentenextraktion via LLM) werden diese Dokumente nun automatisiert ausgelesen, mit dem ERP-Katalog abgeglichen und als validierter Auftragsvorschlag ins System eingespielt. Der Mitarbeiter prüft lediglich noch Ausnahmefälle und klickt auf „Buchen“.

* **Zeitaufwand neu:** 15 Minuten pro Mitarbeiter/Tag = 45 Minuten/Tag (ca. 15 Stunden/Monat).
* **Ersparnis:** 135 Stunden/Monat bzw. **6.480 Euro monatlich**.
* **Implementierungskosten (Setup & Integration):** Einmalig 14.500 Euro.

Der **Amortisationszeitpunkt (Break-even)** war nach exakt 2,24 Monaten erreicht. Noch entscheidender als die reine Kostenreduktion: Die Reaktionszeit auf Kundenanfragen sank von durchschnittlich 36 Stunden auf unter 4 Stunden – was die Angebots-Abschlussquote im ersten Quartal messbar um 12 % steigerte.

#### Die ROI-Formel für Ihr Haus

Berechnen Sie den potenziellen Ertrag vor jedem Projektstart nach dieser Formel:

$$\text{ROI (Monate)} = \frac{\text{Einmalkosten Setup} + (\text{Monatliche Betriebskosten} \times 12)}{(\text{Eingesparte Arbeitsstunden/Monat} \times \text{Stundensatz}) \times 12 - \text{Laufende Toolkosten}}$$

Liegt der kalkulierte Break-even über 6 Monaten, verwerfen Sie den Use Case vorerst. Suchen Sie nach Prozessen mit spitzerem Hebel.

---

## 3. Verkaufspreis-Vorschlag & Vertriebsplattform

### Preismodell (B2B-Positionierung)
Mittelständische Entscheider bewerten Qualität stark über den Preis. Ein Preis von 9,99 € signalisiert Konsumentenliteratur ohne Umsetzungsrelevanz.

* **Standard-Edition (E-Book als PDF/ePub):** **79,00 € zzgl. MwSt.**  
  *(Positionierung als Fachbuch / digitaler Leitfaden für Führungskräfte)*
* **Business-Edition (E-Book + Excel-ROI-Kalkulator + DSGVO-Checklisten & Muster-Verfahrensverzeichnis):** **149,00 € zzgl. MwSt.**  
  *(Erwarteter Bestseller durch sofort einsetzbare Arbeitshilfen)*
* **Team-/Unternehmenslizenz (bis zu 10 Zugänge + Video-Einführung):** **390,00 € zzgl. MwSt.**

### Plattform-Empfehlung: Digistore24 oder Elopage
* **Begründung:** 
  1. **Rechtssicherheit & Steuern im DACH-Raum:** Beide Plattformen agieren als Reseller (Merchant of Record). Sie übernehmen die korrekte steuerliche Abwicklung (EU-B2B-Reverse-Charge, deutsche USt.) und stellen ordentliche B2B-Rechnungen mit ausgewiesener USt-IdNr. aus.
  2. **Zahlungsarten:** B2B-Käufer im Mittelstand bevorzugen SEPA-Lastschrift, Firmenkreditkarte und Kauf auf Rechnung. Beide Anbieter decken dies out-of-the-box ab.
  3. **Upsell-Funnels:** Technisch nahtlose 1-Click-Upsells zur direkten Konvertierung von Buchkäufern in den hochpreisigen Videokurs.

---

## 4. Upsell-Produkt: Kurs-Gliederung (5 Module)

### Kurstitel
**KI-Executive: Der 6-Wochen-Blueprint für operative Exzellenz im Mittelstand**  
*Format: Video-Lektionen, wöchentliche Office Hours, Vorlagen & Code-Snippets (Zielpreis: 990,00 € bis 1.490,00 € netto).*

* **Modul 1: Strategische Priorisierung & Business Case**
  * Ableitung der 3 wichtigsten Pilotprojekte anhand der Unternehmensziele
  * Exakte Budgetierung von Token-Kosten, Infrastruktur und Integrationsaufwänden
  * Stakeholder-Alignment: Den Beirat und Gesellschafterkreis überzeugen

* **Modul 2: IT-Architektur, Sicherheit & DSGVO im Detail**
  * Architekturmuster: Cloud-API vs. On-Premise/Private-Cloud-Hosting
  * Datenanonymisierung und PII-Filterung vor Modellübergabe
  * Verträge zur Auftragsverarbeitung (AVV) mit KI-Anbietern wasserdicht aufsetzen

* **Modul 3: Das interne Firmenwissen erschließen (RAG-Deepdive)**
  * Bestandsaufnahme: ERP, CRM, Netzlaufwerke und Wiki strukturieren
  * Auswahl von Embeddings und Vektordatenbanken (Pinecone, Qdrant, Chroma)
  * Vermeidung von Halluzinationen und Einrichten von Quellenangaben-Pflicht

* **Modul 4: Workflows automatisieren mit Make, n8n und LLM-Agents**
  * No-Code/Low-Code-Automatisierung für Sachbearbeitungsprozesse
  * Fallstricke bei Schnittstellen (APIs) zu Legacy-ERP-Systemen (SAP, Navision/Business Central)
  * Human-in-the-Loop-Freigabeprozesse per MS Teams oder Slack

* **Modul 5: Unternehmenskultur, Enablement & Skalierungsphase**
  * Rollenprofile: Den internen „KI-Promotor“ identifizieren und ausbilden
  * Richtlinien für Mitarbeiter (KI-Policy) transparent kommunizieren
  * Kontinuierliches Monitoring von Kosten, Antwortqualität und Fehlerquoten
