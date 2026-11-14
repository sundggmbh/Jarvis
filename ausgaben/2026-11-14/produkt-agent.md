# Arbeitsprobe: produkt-agent

# Produkt-Dossier: Digitales Infoprodukt für den Mittelstand
**Erstellt durch:** Produkt-Agent, Jarvis GmbH  
**Status:** Verkaufsfertige Konzeption & Muster-Kapitel

---

## 1. E-Book: Titel & Inhaltsverzeichnis

### Produkttitel
**Der KI-Fahrplan für den Mittelstand**  
*Wie Sie operative Prozesse ohne Großbudget pragmatisch automatisieren, Kosten senken und Fachkräfte entlasten.*

### Zielgruppe
Geschäftsführer, COOs, IT-Leiter und Abteilungsleiter in mittelständischen Unternehmen (50–500 Mitarbeiter) im DACH-Raum.

### Inhaltsverzeichnis (8 Kapitel)
* **Kapitel 1: Realitätscheck – Wo KI im Mittelstand wirklich Rendite bringt**  
  *Abgrenzung zwischen Hype und operativer Realität; 5 typische Fehlinvestitionen vermeiden.*
* **Kapitel 2: Die Prozess-Inventur: Low-Hanging Fruits identifizieren**  
  *Audit-Framework für Routineaufgaben in Vertrieb, Kundenservice, Einkauf und HR.*
* **Kapitel 3: Der schlanke KI-Stack: Werkzeuge ohne monatelange IT-Projekte**  
  *DSGVO-fähige LLM-Lösungen, Middleware (Make/Zapier) und No-Code-Datenbanken im Praxiseinsatz.*
* **Kapitel 4: Compliance & Rechtssicherheit: DSGVO, Betriebsrat und Geschäftsgeheimnisse**  
  *Sichere Datenräume, Auftragsverarbeitungsverträge (AVV) und klare Nutzungsrichtlinien für Belegschaften.*
* **Kapitel 5: Das 30-Tage-Pilotprojekt: Vom ersten Prompt zum stabilen Workflow**  
  *(Muster-Kapitel – siehe Abschnitt 2)*
* **Kapitel 6: Mitarbeiter mitnehmen: Change-Management statt Technologie-Schock**  
  *Wie Sie Skepsis abbauen, Prompt-Kompetenz aufbauen und interne Power-User etablieren.*
* **Kapitel 7: Skalierung & Governance: Von der Einzellösung zum vernetzten System**  
  *Aufbau einer unternehmenseigenen Prompt- und Workflow-Bibliothek; Schnittstellen zu ERP und CRM.*
* **Kapitel 8: ROI-Messung und strategischer Ausblick**  
  *KPI-Dashboard zur Zeiterfassung; Amortisationsrechnung und Vorbereitung auf multimodale Agentensysteme.*

---

## 2. Vollständig ausgeschriebenes Muster-Kapitel

### Kapitel 5: Das 30-Tage-Pilotprojekt: Vom ersten Prompt zum stabilen Workflow

Ein häufiger Fehler mittelständischer Unternehmen bei der Einführung künstlicher Intelligenz ist der Versuch, sofort die perfekte Komplettlösung zu etablieren. Das führt unweigerlich zu überdehnten Budgets, frustrierten Fachabteilungen und Projekten, die im Sande verlaufen. Erfolgreiche KI-Adaption folgt stattdessen dem Prinzip des kleinsten wirksamen Eingriffs (*Minimum Viable Automation*). 

Ziel dieses 30-Tage-Plans ist es, innerhalb eines Monats genau **einen** wiederkehrenden Prozess vollständig zu automatisieren, messbare Zeiteinsparungen zu belegen und das Vertrauen des Teams zu gewinnen.

#### Woche 1: Selektion und Messbasis (Tag 1 bis 7)
Wählen Sie für den Piloten keinen geschäftskritischen Kernprozess mit direktem Kundenkontakt aus. Ideal sind interne, repetitive Informationsprozesse: beispielsweise die tägliche Vorqualifizierung eingehender Lieferantenanfragen, das Extrahieren von Spezifikationen aus PDF-Ausschreibungen oder die Erstellung von Standard-Zusammenfassungen aus wöchentlichen Vertriebsberichten.

Definieren Sie an Tag 1 eine Baseline:
1. Wie viele Minuten benötigt ein Mitarbeiter heute pro Vorgang?
2. Wie hoch ist das monatliche Volumen?
3. Welche Fehlerquote tritt üblicherweise auf?

Halten Sie diese drei Kennzahlen schriftlich fest. Sie bilden die Grundlage für Ihre spätere ROI-Berechnung.

#### Woche 2: Der manuelle Prototyp (Tag 8 bis 14)
Beginnen Sie nicht mit komplexen API-Verbindungen. In dieser Woche testet eine einzige Person den Prozess händisch über ein geschütztes Firmenkonto eines DSGVO-konformen LLM-Anbieters. 

Erstellen Sie den ersten System-Prompt. Ein robuster Prompt für mittelständische Prozesse folgt stets dem Dreiklang: **Rolle – Kontext – Ausgabeformat**.
* *Rolle:* „Du bist technischer Einkaufsassistent der Jarvis Maschinenbau GmbH.“
* *Kontext:* Übergeben Sie die Rohdaten (anonymisiert) mit klaren Ausschlusskriterien.
* *Ausgabeformat:* Verlangen Sie strukturierte Tabellen oder JSON-Dateien, keine Fließtexte.

Testen Sie mindestens 20 reale Fälle der Vergangenheit und optimieren Sie die Instruktionen, bis die Trefferquote bei über 90 % liegt.

#### Woche 3: Die technische Brücke (Tag 15 bis 21)
Nun wird der manuelle Kopiervorgang eliminiert. Binden Sie den optimierten Prompt über eine No-Code-Integrationsplattform (beispielsweise Make oder n8n auf eigenem Server) an Ihre bestehende Infrastruktur an. 

Der Datenfluss: Eingehende E-Mail mit Anhang $\rightarrow$ Automatischer Trigger $\rightarrow$ Bereinigung und DSGVO-Filterung $\rightarrow$ KI-Verarbeitung via API $\rightarrow$ Rückgabe an Ihr ERP oder ein geteiltes Dashboard.

Bauen Sie zwingend eine *Human-in-the-Loop*-Schleife ein: Die KI trifft im Piloten keine finalen Entscheidungen, sondern liefert einen unterschriftsreifen Entwurf, den der zuständige Sachbearbeiter mit einem Klick freigibt oder korrigiert.

#### Woche 4: Validierung, Härtung und Go-Live (Tag 22 bis 30)
Im letzten Schritt arbeitet der zuständige Mitarbeiter fünf Werktage im Produktivbetrieb mit dem neuen Workflow. Messen Sie nun erneut die Kennzahlen aus Woche 1.

Verfassen Sie am 30. Tag einen zweiseitigen Ergebnisbericht für die Geschäftsführung: Zeigen Sie die eingesparten Netto-Arbeitsstunden und die Akzeptanzquote des Nutzers. Ein erfolgreicher Pilot mit 70 % Zeitersparnis ist Ihr stärkstes Argument, um das Budget für die unternehmensweite Skalierung freizugeben.

*(Wortanzahl Kapitel: ca. 450 Wörter)*

---

## 3. Preis- und Plattformstrategie

### Preisgestaltung
Im Mittelstands-B2B-Segment deuten "Konsumentenpreise" (z. B. 9,99 €) auf minderwertigen Inhalt hin und senken die Kaufbereitschaft.

* **Standard-Lizenz (E-Book als PDF/ePub):** **79,00 € zzgl. USt.**  
  *Positionierung als Fachliteratur/Arbeitswerkzeug, problemlos über Betriebsausgaben abrechenbar.*
* **Business-Bundle (E-Book + Prompt-Vorlagen + DSGVO-Checklisten + Make-Blueprints):** **149,00 € zzgl. USt.**

### Plattform-Empfehlung
* **Primärempfehlung:** **Digistore24** oder **Copecart** (als Reseller-Modell).
  * *Begründung:* Vollständige Abwicklung von Rechnungsstellung mit Ausweis der USt. für Deutschland, Österreich und Schweiz. Übernahme der Haftung für Steuern und automatische Bereitstellung ordnungsgemäßer B2B-Rechnungen (Pflicht für deutsche Buchhaltungen).
* **Alternative (bei vorhandener technischer Basis):** Eigener Shop via **Shopify / WooCommerce + Stripe**.
  * *Vorteil:* Volle Kontrolle über Kundendaten und Branding, keine Reseller-Margen (ca. 7–10 % Ersparnis pro Transaktion).

---

## 4. Upsell-Produkt: Kurs-Gliederung

### Produkttitel
**B2B-Masterclass: KI-Prozessarchitektur für KMU**  
*Der 5-Wochen-Videokurs mit Live-Q&A zur Implementierung autonomer Workflows.*  
*Preisempfehlung:* **890,00 € bis 1.490,00 € zzgl. USt.** (inkl. 2 Team-Plätzen).

### Modulübersicht

* **Modul 1: Technische Infrastruktur & Souveränität**
  * Lokale vs. Cloud-Modelle (OpenAI Enterprise, Azure AI Services, Mistral/Llama on-premises).
  * Berechtigungs- und Rollenkonzepte: So verlassen Unternehmensdaten nicht den geschützten Raum.
  * *Deliverable:* Sicherheitsmatrix zur Freigabe durch den betrieblichen Datenschutzbeauftragten.

* **Modul 2: Advanced Prompt Engineering & Datenextraktion**
  * Strukturierte Datenausgabe (JSON, XML) für die fehlerfreie Weiterverarbeitung in Altsystemen.
  * Few-Shot-Prompting und Chain-of-Thought für komplexe kaufmännische Prüfprozesse.
  * *Deliverable:* Die Jarvis-Prompt-Bibliothek mit 40 einsatzbereiten B2B-Vorlagen.

* **Modul 3: Workflow-Automatisierung mit No-Code & Webhooks**
  * Praxiseinrichtung von Integrations-Engines (Fokus: n8n für deutsche Datenhoster).
  * Anbindung von Microsoft 365, Google Workspace und gängigen ERP-Systemen (z. B. SAP, Datev, Weclapp via REST-API).
  * *Deliverable:* 3 importfertige Workflow-Dateien (.json) für Standardprozesse.

* **Modul 4: Wissensmanagement mit RAG (Retrieval-Augmented Generation)**
  * Aufbau einer internen Unternehmens-Wissensdatenbank (Wikis, Verfahrensanweisungen, Produktkataloge).
  * Vermeidung von "Halluzinationen": Quellengenaues Antworten sicherstellen.
  * *Deliverable:* Schritt-für-Schritt-Setup eines firmeninternen Frage-Antwort-Bots.

* **Modul 5: Monitoring, Qualitätssicherung und Governance**
  * Automatisches Logging von KI-Antworten und Fehlerraten.
  * Erstellung interner Betriebsvereinbarungen und Schulungskonzepte für Mitarbeiter.
  * *Deliverable:* Muster-Betriebsvereinbarung „Nutzung generativer KI am Arbeitsplatz“.
