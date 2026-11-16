# Arbeitsprobe: produkt-agent

# Produkt-Exposé & Arbeitsprobe: Digitales B2B-Informationsprodukt

**Erstellt durch:** Produkt-Agent | Jarvis GmbH  
**Zielgruppe:** Inhaber, Geschäftsführer und operative Leiter (COO/CFO) im deutschsprachigen Mittelstand (50–500 Mitarbeiter).  
**Wertversprechen:** Praxisnahe, pragmatische Implementierung von KI und No-Code-Automatisierung ohne teure Enterprise-Berater oder monatelange IT-Projekte.

---

## 1. E-Book: Titel & Inhaltsverzeichnis

**Titel:**  
*Der KMU-Automations-Leitfaden: Wie der Mittelstand Routineaufgaben halbiert, Fachkräfte entlastet und KI ohne Millionenbudget einführt*

**Untertitel:**  
*Das Praxis-Handbuch für Geschäftsführer und Betriebsleiter: Von der Prozessanalyse bis zum produktiven Rollout in 60 Tagen.*

### Inhaltsverzeichnis

* **Vorwort:** Warum Pragmatismus die deutsche Digitalisierungsstarre bricht
* **Kapitel 1: Bestandsaufnahme ohne Illusionen**
  * Wo mittelständische Unternehmen wirklich Zeit verlieren (Papier, Medienbrüche, Excel-Friedhöfe)
  * Die drei typischen Denkfehler bei der Digitalisierung
* **Kapitel 2: Das Baukasten-Prinzip statt SAP-Großprojekt**
  * Schnittstellen (APIs), No-Code-Tools (Make, n8n) und Large Language Models (LLMs)
  * Datenschutz & DSGVO-Konformität: Lokale Modelle vs. Cloud-APIs mit Auftragsverarbeitungsvertrag (AVV)
* **Kapitel 3: Die 80/20-Prozessanalyse: Welche 3 Kernprozesse Sie zuerst automatisieren sollten** *(Musterkapitel)*
  * Kriterien: Frequenz, Fehleranfälligkeit, Standardisierungsgrad
  * Die „Schmerz-Matrix“ für Abteilungsleiter
* **Kapitel 4: Use Case 1 – Der automatisierte Posteingang & Rechnungsverarbeitung**
  * Von PDF zu ERP: Rechnungsprüfung, Kontierung und Freigabe-Workflows ohne manuelles Abtippen
* **Kapitel 5: Use Case 2 – Vertriebsinnendienst & Angebotswesen**
  * KI-gestützte Angebotserstellung aus unstrukturierten Kundenanfragen (E-Mail/Telefonnotiz)
* **Kapitel 6: Use Case 3 – Kundenservice & Reklamationsmanagement**
  * Automatisierte Vorsortierung, Sentiment-Analyse und Ticket-Zuweisung mit Eskalationsregeln
* **Kapitel 7: Change Management im Betrieb: Ängste abbauen, Mitarbeiter mitnehmen**
  * Kommunikation: Vom „Arbeitsplatzvernichter“ zum „digitalen Werkstudenten“
  * Anreizsysteme für Prozessinnovation aus den eigenen Reihen
* **Kapitel 8: Die 60-Tage-Roadmap**
  * Schritt-für-Schritt-Plan zur ersten produktiven Automation innerhalb von zwei Monaten
* **Anhang:** Tool-Vergleich, DSGVO-Checkliste und Vorlagen zur Prozessdokumentation

---

## 2. Vollständig ausgeschriebenes Muster-Kapitel

### Kapitel 3: Die 80/20-Prozessanalyse: Welche 3 Kernprozesse Sie zuerst automatisieren sollten

Wenn Geschäftsführer mich fragen: *„Wo fangen wir an?“*, lautet meine Gegenfrage fast immer: *„Welche Aufgabe sorgt am Montagmorgen in Ihrem Innendienst für das tiefste Stöhnen?“*

Der größte Fehler, den mittelständische Unternehmen bei der Einführung von Automatisierung und KI begehen, ist der Versuch, den gesamten Betrieb auf einen Schlag zu revolutionieren. Wer sofort das gesamte ERP-System ersetzen oder eine allwissende Unternehmens-KI bauen will, produziert vor allem zwei Dinge: explodierende Beraterkosten und resignierte Mitarbeiter.

Erfolgreiche Automatisierung folgt im Mittelstand dem Pareto-Prinzip. Wir suchen 20 Prozent des Arbeitsaufwands, die für 80 Prozent der manuellen Reibungsverluste verantwortlich sind. 

#### Die drei Filter für den perfekten Erstprozess

Ein Prozess eignet sich genau dann hervorragend für das erste Pilotprojekt, wenn er drei spezifische Kriterien erfüllt:

1. **Hohe Wiederholrate (Frequenz):** Der Vorgang findet nicht einmal im Monat statt, sondern täglich mindestens fünf bis zehn Mal.
2. **Geringe strategische Ambiguität:** Die Regeln sind zu 90 Prozent klar definiert: *„Wenn Bedingung A zutrifft, folgt Aktion B.“*
3. **Vorhandensein unstrukturierter Daten:** Genau hier spielt moderne KI ihre Stärke aus. Das Lesen von E-Mails, das Extrahieren von Daten aus Lieferscheinen oder das Zusammenfassen von PDF-Anhängen war vor wenigen Jahren noch hochkomplex – heute ist es gelöste Technologie.

#### Die „Schmerz-Matrix“: Finden statt Raten

Bitten Sie Ihre Abteilungsleiter nicht um eine theoretische Wunschliste. Nutzen Sie stattdessen für fünf Arbeitstage die **Schmerz-Matrix**: Jeder Mitarbeiter im operativen Kern notiert Tätigkeiten, die folgende Eigenschaften aufweisen:
* Daten von System A (z. B. einer E-Mail oder einem PDF) manuell in System B (z. B. ERP oder CRM) abtippen.
* Wiederkehrende Statusfragen beantworten (*„Ist die Ware schon raus?“, „Wann kommt das Angebot?“*).
* Dokumente formal auf Vollständigkeit prüfen.

Aus den Rückmeldungen kristallisieren sich in 90 Prozent der Industrie- und Handelsunternehmen drei typische Startkandidaten heraus:

1. **Auftrags- und Bestellerfassung:** Ein Kunde schickt eine Bestellung als PDF-Scan. Statt dass ein Vertriebsmitarbeiter 15 Minuten lang Artikelnummern, Stückzahlen und Lieferadressen händisch in die Maske hämmert, übernimmt ein OCR- und LLM-Parser diesen Schritt. Der Mensch prüft im Anschluss nur noch das Ergebnis und gibt die Freigabe per Klick.
2. **Rechnungsfreigabe und Belegzuordnung:** Eingangsrechnungen werden automatisiert aus Postfächern extrahiert, mit Bestellungen abgeglichen und bei Übereinstimmung direkt vorkontiert an die Buchhaltung übergeben.
3. **Vorbereitung technischer Anfragen:** Eingehende Ausschreibungen oder Spezifikationen werden automatisch zusammengefasst und mit dem internen Produktkatalog abgeglichen, bevor der Vertriebsingenieur die Datei überhaupt öffnet.

#### Das Ziel des ersten Projekts

Ihr erstes Automatisierungsprojekt muss nicht perfekt sein – es muss **spürbar** sein. Es soll Zeit zurückgeben: nicht in sechs Monaten, sondern in drei Wochen. Wenn Ihr Team merkt, dass ihnen die Technologie lästige Routinearbeit abnimmt, schlägt Skepsis in Neugier um. Das ist der Moment, in dem die digitale Transformation in Ihrem Betrieb zum Selbstläufer wird.

---

## 3. Verkaufspreis-Vorschlag & Plattform

### Preismodell
* **Verkaufspreis E-Book (Einzelprodukt):** **67,- € netto** (B2B-Standard, ca. 79,73 € inkl. MwSt.)
* **Begründung:** Ein Preis unter 50 € signalisiert im B2B-Bereich oft minderwertigen Content („Amazon Kindle Ratgeber“). Ein Preis von 67 € ist eine schmerzfreie Ausgabe über Firmen-Kreditkarte/Spesen, selektiert aber zahlungskräftige Entscheider vor, die echtes Umsetzungsinteresse haben.

### Empfohlene Plattform & Checkout
* **Empfehlung:** **Digistore24** oder **Copecart** (Reseller-Modell)
  * **Vorteil:** Übernimmt die vollständige Rechnungsstellung mit korrekter MwSt.-Abwicklung (Reverse-Charge für AT/CH, B2B-Steuer-IDs in DE) sowie Mahnwesen.
  * **Alternativ für volles Branding:** Eigener Shop via **Shopify** mit Anbindung an **Stripe** und automatischer Belegerstellung über *Lexoffice* oder *Billbee*.

---

## 4. Upsell-Produkt: B2B-Video-Masterclass

**Titel:** *KMU-Automation-Masterclass: Der 6-Wochen-Blueprint zur No-Code- & KI-Integration*  
**Format:** 5 Module (On-Demand-Videos), SOP-Vorlagen, Make/n8n-Code-Snippets, wöchentlicher Live-Q&A-Call.  
**Upsell-Preis:** **990,- € netto** (Einmalzahlung) oder 3x 360,- € (Order-Bump im E-Book-Funnel oder Follow-up-E-Mail-Sequenz).

### Kurs-Gliederung (5 Module)

* **Modul 1: Architektur & DSGVO-konforme Infrastruktur für KMU**
  * Auswahl des Tool-Stacks: Make (Cloud) vs. n8n (Self-Hosted auf deutschen Servern)
  * Sichere Anbindung von OpenAI/Anthropic/Open-Source-Modellen mit rechtskonformen AV-Verträgen
  * Rechte- und Rollenmanagement: Wer darf welche Daten automatisieren?

* **Modul 2: Die digitale Poststelle: Dokumente & Belege automatisiert verarbeiten**
  * Schritt-für-Schritt-Bau einer Pipeline: E-Mail-Eingang $\to$ KI-Extraktion $\to$ ERP-Übergabe
  * Validierungsschleifen (Human-in-the-Loop): Wie Mitarbeiter mit einem Klick Ausnahmen korrigieren
  * Fallbeispiel: Verarbeitungszeit von Eingangsrechnungen von 12 auf 2 Minuten senken

* **Modul 3: Vertriebs- und CRM-Automatisierung**
  * Eingehende Leads automatisch anreichern, priorisieren und dem richtigen Vertriebler zuweisen
  * Automatisierte Entwurfserstellung für Angebote basierend auf Standardkatalogen
  * Synchronisation von Silo-Daten (z. B. E-Mail-Postfächer zu HubSpot/Pipedrive/Eigenbau-CRM)

* **Modul 4: Interne Firmen-KI: Sicheres Wissensmanagement (RAG-System)**
  * Aufbau einer internen Wissensdatenbank für Mitarbeiter (Handbücher, Verfahrensanweisungen, ISO-Dokus)
  * Keine Datenweitergabe an Dritte: Einrichten lokaler Embeddings
  * Anwendungsfall: Schnelleres Onboarding neuer Fachkräfte und Schichtübergaben in der Produktion

* **Modul 5: Governance, Monitoring & Skalierung**
  * Error-Handling: Was passiert, wenn eine Schnittstelle ausfällt? (Notfall-Routinen)
  * Monitoring-Dashboards für den Geschäftsführer: Zeiteinsparung und ROI messbar machen
  * Etablierung eines internen „Automation Hubs“: Wie Mitarbeiter kontinuierlich eigene Abläufe optimieren
