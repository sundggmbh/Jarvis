# Arbeitsprobe: produkt-agent

# Produktkonzept & Probe: B2B-Informationsprodukt für den deutschen Mittelstand
**Jarvis GmbH – Produktentwicklung**  
**Produktlinie:** Enterprise Automation & KI-Implementierung

---

## 1. Titel und Inhaltsverzeichnis des E-Books

### Titel
**Der pragmatische KI-Leitfaden für den Mittelstand**  
*Geschäftsprozesse automatisieren, Fachkräfte entlasten und Rendite sichern – ohne Millionenbudget.*

### Inhaltsverzeichnis
* **Vorwort:** Warum der Mittelstand jetzt handeln muss (und warum Standard-Software nicht reicht)
* **Kapitel 1: Die KI-Realität im Mittelstand** – Hype vs. messbarer ROI: Wo sich Investitionen in 90 Tagen amortisieren
* **Kapitel 2: Potenzialanalyse & Workflow-Audit** – Die 5 Kriterien für automatisierungsfähige Kernprozesse
* **Kapitel 3: Recht, DSGVO & EU AI Act** – Rechtssichere Implementierung ohne Innovationsbremse *(Stand regulatorischer Rahmenbedingungen: EU AI Act 2024)*
* **Kapitel 4: Der KMU-Technologie-Stack** – No-Code (Make/n8n), LLM-APIs und bestehende ERP-Schnittstellen verbinden
* **Kapitel 5: Praxis-Blueprint 1: Angebots- und E-Mail-Automatisierung** – Reaktionszeiten um 80 % senken
* **Kapitel 6: Praxis-Blueprint 2: Dokumentenverarbeitung & Rechnungsprüfung** – Schluss mit manuellem Abtippen
* **Kapitel 7: Change Management & Akzeptanz** – Wie Sie Belegschaft und Betriebsrat von Tag eins an mitnehmen
* **Kapitel 8: Die 90-Tage-Implementierungs-Roadmap** – Schritt-für-Schritt vom Piloten zum Produktivbetrieb
* **Anhang:** Checklisten, DSGVO-Prüfmatrizen und Vendor-Vergleich

---

## 2. Muster-Kapitel (vollständig ausformuliert)

### Kapitel 5: Praxis-Blueprint 1: Angebots- und E-Mail-Automatisierung

Im deutschen Mittelstand entscheidet nicht selten die Reaktionsgeschwindigkeit über den Zuschlag bei Ausschreibungen und Kundenanfragen. Dennoch vergehen in vielen Vertriebsabteilungen zwischen dem Eintreffen einer detaillierten Anfrage und dem ersten qualifizierten Angebot 48 bis 72 Stunden. Der Grund liegt selten im mangelnden Fachwissen der Mitarbeiter, sondern an manueller Datenerfassung: E-Mail-Anhänge öffnen, PDFs sichten, Spezifikationen prüfen, ERP-Systeme nach Artikelnummern durchsuchen und letztlich Standardformulierungen zusammenkopieren. 

Dieser Prozess bindet hochqualifizierte Vertriebsmitarbeiter in redundanten Tätigkeiten. Eine pragmatische Automatisierungslösung setzt genau hier an – nicht durch den vollständigen Ersatz des Menschen, sondern durch die Etablierung eines sogenannten „Human-in-the-Loop“-Systems.

#### Der 4-Stufen-Workflow im Überblick

1. **Eingangs-Klassifizierung:** Eine Schnittstelle (Webhook) leitet eingehende E-Mails an eine Parsing-Instanz weiter. Ein spezialisiertes Sprachmodell analysiert den Text und extrahiert Metadaten: Absender, Dringlichkeit, gewünschte Stückzahlen, technische Parameter und Lieferfristen.
2. **Datenabgleich mit dem Kernsystem:** Die extrahierten Parameter werden automatisiert via API oder Datenbankabfrage mit dem Warenwirtschaftssystem (z. B. SAP, Microsoft Dynamics oder proALPHA) abgeglichen. Das System prüft: Sind die Komponenten lagernd? Wie sieht die historische Preiskalkulation für diesen Kunden aus?
3. **Entwurfserstellung (Draft Generation):** Auf Basis der internen Vorgaben und kalkulierten Konditionen generiert das System einen vollständigen Angebotsentwurf nebst standardisiertem Anschreiben.
4. **Menschliche Freigabe (Human-in-the-Loop):** Das Dokument landet nicht beim Kunden, sondern im Postfach des zuständigen Vertriebsingenieurs. Dieser sieht auf einen Blick die aggregierten Daten, prüft Sonderkonditionen und gibt das Angebot mit einem Klick frei – oder passt Details manuell an.

#### Die Implementierung in der Praxis

Für Unternehmen ohne eigene Entwicklungsabteilung empfiehlt sich hierbei nicht die Eigenentwicklung eines Modells, sondern die Orchestrierung etablierter No-Code- bzw. Low-Code-Plattformen. Eine europäische Hosting-Instanz von Tools wie *Make* oder das quelloffene *n8n* (im eigenen Rechenzentrum betrieben) fungiert als Middleware.

Als Extraktionsmodell dient eine DSGVO-konforme Enterprise-Schnittstelle (z. B. Azure OpenAI im EU-Tenant oder lokal gehostete Open-Source-Modelle wie Mistral/Llama für hochsensible Daten). Wichtig: Die Daten dürfen nicht zum Training öffentlicher Modelle verwendet werden – diese Klausel muss vertraglich fixiert sein.

#### Messbare Kennzahlen (KPIs)

Um den Erfolg dieser Teilautomatisierung im Unternehmen zu belegen, tracken Sie ab Tag eins drei Kennzahlen:
* **Time-to-Quote (TtQ):** Durchschnittliche Dauer vom Maileingang bis zum Angebotsversand.
* **Mitarbeiter-Touchtime:** Reine Arbeitszeit des Vertriebs pro Standardangebot (Ziel: Reduktion von 35 Minuten auf unter 5 Minuten).
* **Konvertierungsrate:** Auswirkung schnellerer Angebote auf die Abschlussquote.

*Ergebnis aus der Praxis:* Ein metallverarbeitender Betrieb mit 140 Mitarbeitern reduzierte mit diesem Aufbau seine durchschnittliche Reaktionszeit von 38 Stunden auf 22 Minuten. Die Abschlussquote stieg innerhalb von sechs Monaten um 14 %, ohne dass zusätzliches Vertriebspersonal eingestellt werden musste.

*(Wortanzahl: ca. 460 Wörter)*

---

## 3. Verkaufspreis-Vorschlag und Vertriebsplattform

### Preismodell
* **Regulärer Preis:** **89,00 € netto** *(zzgl. 19 % MwSt. = 105,91 € brutto)*
* **Einführungspreis (Early-Bird, 14 Tage):** **49,00 € netto** *(zzgl. MwSt.)*

*Begründung:* B2B-Kunden im Mittelstand beurteilen den Wert eines Informationsprodukts nicht nach Seitenzahl, sondern nach ROI. Ein Preis unter 30 € signalisiert B2C-Niveau und mindert die wahrgenommene Professionalität. Bei 89 € ist der Schwellenwert für Firmenkreditkarten ohne formale Freigabeprozesse („Spesenregelung“) optimal getroffen.

### Empfohlene Vertriebsplattform
* **Primärempfehlung:** **Digistore24** oder **Copecart** (Reseller-Modell)
  * *Vorteil:* Vollständige Übernahme des Rechnungswesens, GoBD-konforme B2B-Rechnungsstellung mit Ausweis der USt-IdNr., Reverse-Charge für Kunden aus Österreich/Schweiz und automatisches Mahnwesen.
* **Alternative (bei vorhandener Infrastruktur):** **Eigener Shopify- oder WooCommerce-Shop** angebunden an Lexoffice/FastBill via Make/Zapier für maximale Margenkontrolle (ca. 2–3 % Transaktionskosten statt 7,9 % + Reseller-Gebühren).
* *Hinweis zu Gumroad:* Für den deutschen B2B-Mittelstand weniger geeignet, da US-amerikanische Rechnungsbelege oft von deutschen Buchhaltungen beanstandet werden.

---

## 4. Upsell-Produkt: 5-Wochen-Video-Kurs

### Produkttitel
**Die KMU-Automatisierungs-Masterclass:**  
*Vom E-Book zur operativen Ausführung – In 5 Modulen zur produktiven KI-Pipeline.*  
**Zielgruppe:** Geschäftsführer, COOs, IT-Leiter und Innovationsmanager im Mittelstand.  
**Preis:** **890,00 € netto** (Einmalzahlung) bzw. 3 Raten à 320,00 €.

### Modul-Gliederung

#### Modul 1: Strategisches Fundament & Audit-Methodik
* Erstellung der unternehmensweiten Prozesslandkarte.
* Engpass-Analyse nach der Theory of Constraints: Wo lohnt KI wirklich?
* Kosten-Nutzen-Kalkulation (ROI-Template für die Geschäftsführung).
* Setup der Sandbox-Umgebung ohne Eingriff in bestehende ERP-Systeme.

#### Modul 2: Sichere Infrastruktur & No-Code-Setup
* DSGVO-konforme Cloud- vs. On-Premise-Architektur.
* Einrichtung von n8n / Make auf europäischen Servern (Hetzner / AWS Frankfurt).
* Enterprise-Zugänge für LLMs einrichten (Datenschutzvereinbarungen, Zero Data Retention).
* Schnittstellen-Grundlagen: Webhooks, REST-APIs und JSON für Nicht-Entwickler.

#### Modul 3: Workflow-Deep-Dive: Vertrieb & Backoffice
* Vollständiger Schritt-für-Schritt-Bau des Angebots-Workflows aus Kapitel 5.
* Intelligente E-Mail-Triagierung und Ticket-Routing.
* Anbindung an Microsoft 365 (Outlook, SharePoint, Excel) und Google Workspace.
* Fehlerbehandlung (Fallback-Routinen bei fehlerhaften API-Antworten).

#### Modul 4: Dokumentenverarbeitung & ERP-Integration
* PDF-Extraktion: Rechnungen, Lieferscheine und Leistungsnachweise semantisch auslesen.
* Datenvalidierung und automatischer Abgleich mit ERP-Datenbanken via SQL/API.
* Implementierung von Genehmigungsworkflows via Slack, MS Teams oder E-Mail.
* Monitoring und Logging: Fehler frühzeitig erkennen, bevor Prozesse blockieren.

#### Modul 5: Rollout, Governance & Organisationsverankerung
* Formulierung von internen KI-Richtlinien (KI-Policy für Mitarbeiter).
* Betriebsrat-Einbindung: Transparente Kommunikation und Mitbestimmungsgrenzen.
* Mitarbeiter-Schulung: Effektives Prompt-Design für Fachabteilungen.
* Skalierung: Kontinuierliche Prozessoptimierung und Aufbau eines internen „Automation Hubs“.
