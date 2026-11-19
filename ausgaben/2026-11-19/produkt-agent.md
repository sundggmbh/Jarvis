# Arbeitsprobe: produkt-agent

# Produkt-Dossier: B2B-Informationsprodukt für den Mittelstand

**Agentur / Herausgeber:** Jarvis GmbH  
**Produktlinie:** Enterprise Operations & AI Acceleration  

---

## 1. Titel und Inhaltsverzeichnis des E-Books

### Buchtitel
**Der KI-Effizienz-Blueprint: Wie der Mittelstand operative Prozesse automatisiert – ohne IT-Großprojekte und Millionenbudget**

### Inhaltsverzeichnis

* **Vorwort:** Warum Pragmatismus den Mittelstand vor dem IT-Stillstand rettet
* **Kapitel 1: Bestandsaufnahme ohne Illusionen**
  * Wo mittelständische Unternehmen heute Zeit und Marge verbrennen
  * Das 80/20-Prinzip: Administrative Reibungsverluste vs. wertschöpfende Kernkompetenz
* **Kapitel 2: Rechtssicherheit, Datenschutz & DSGVO**
  * Datensicherheit ohne Paralyse: Cloud, On-Premises und EU-Rechenzentren
  * Klare Compliance-Richtlinien für Belegschaft und Geschäftsführung
* **Kapitel 3: Das No-Code- & KI-Technologie-Fundament**
  * ChatGPT Enterprise/Team, Microsoft Copilot & spezialisierte Middleware (z. B. Make.com)
  * Vermeidung von Vendor-Lock-ins und proprietären Sackgassen
* **Kapitel 4: Use Case Einkauf & Rechnungsverarbeitung**
  * Automatisierter Abgleich von Lieferscheinen, Angeboten und PDFs
  * Reduktion von Durchlaufzeiten um 70 %
* **Kapitel 5: Use Case B2B-Vertrieb & Angebotserstellung** *(Muster-Kapitel)*
  * Eingehende Ausschreibungen und Anfragen in Minuten vorqualifizieren
  * Personalisierte, präzise Angebotstexte auf Knopfdruck
* **Kapitel 6: Wissensmanagement & Mitarbeiter-Onboarding**
  * Das „Unternehmens-Gehirn“: Silo-Wissen extrahieren und per internem Chatbot zugänglich machen
  * Einarbeitungszeiten neuer Mitarbeiter halbieren
* **Kapitel 7: Change Management & Mitarbeiter-Befähigung**
  * Ängste vor Rationalisierung abbauen
  * Operative Teams zu internen Automatisierungs-Treibern entwickeln
* **Kapitel 8: Der 90-Tage-Implementierungsplan**
  * Von der Pilotphase zum unternehmensweiten Standard
  * ROI-Messung und Skalierung

---

## 2. Ausgeschriebenes Muster-Kapitel

### Kapitel 5: Use Case B2B-Vertrieb & Angebotserstellung

Im typischen deutschen Mittelstandsunternehmen ist der Vertriebsaußendienst hochqualifiziert, verbringt aber bis zu 40 Prozent seiner Arbeitszeit mit administrativer Fließbandarbeit: Kundendaten erfassen, Lastenhefte manuell nach Spezifikationen durchforsten, CRM-Einträge pflegen und repetitive Begleitbriefe verfassen. Dies bindet genau jene kognitiven Ressourcen, die eigentlich am Verhandlungstisch oder bei der strategischen Neukundengewinnung gebraucht werden.

Die pragmatische KI-Integration setzt genau an dieser Schnittstelle an. Das Ziel ist nicht, den Vertriebsmitarbeiter durch einen Algorithmus zu ersetzen, sondern ihn durch ein intelligentes Assistenzsystem („Copilot“) zu entlasten, das Routineaufgaben in Sekunden abarbeitet.

#### Schritt 1: Die automatisierte Vorqualifizierung (Triage)
Eingehende Anfragen über Kontaktformulare oder E-Mail-Postfächer (`vertrieb@unternehmen.de`) variieren stark in Qualität und Relevanz. Über eine Schnittstelle (mittels Middleware wie Make oder n8n) wird der Text an ein Enterprise-LLM (Großes Sprachmodell) mit spezifischem System-Prompt übergeben. 

Das System prüft innerhalb von Sekundenbruchteilen:
1. Handelt es sich um eine valide Neukundenanfrage, einen bestehenden Vorgang oder Spam?
2. Entspricht das geforderte Volumen den unternehmenseigenen Mindestauftragswerten?
3. Welche Kernkomponenten oder Dienstleistungen werden angefragt?

Das System erzeugt eine standardisierte Zusammenfassung, vergibt einen Lead-Score und legt den Kontakt samt Klassifizierung direkt im CRM-System (z. B. HubSpot, Salesforce oder Pipedrive) an. Unpassende Anfragen werden automatisiert, aber professionell und individuell formuliert, abgewiesen oder an Partner verwiesen.

#### Schritt 2: Extraktion aus unstrukturierten Dokumenten
Erfordert die Anfrage die Analyse von PDF-Anhängen – etwa Ausschreibungsunterlagen oder Spezifikationsblättern –, kommt ein Dokumenten-Parser in Kombination mit Retrieval-Augmented Generation (RAG) zum Einsatz. Anstatt dass ein Senior-Ingenieur ein 60-seitiges Dokument manuell liest, extrahiert das System tabellarisch:
* Geforderte Lieferfristen und Pönalen,
* Technische Toleranzen und Werkstoffvorgaben,
* Kompatibilität mit dem eigenen Produktportfolio.

Abweichungen von den Standard-Lieferbedingungen des Unternehmens werden farblich markiert.

#### Schritt 3: Der Angebotsentwurf auf Knopfdruck
Auf Basis der extrahierten Parameter generiert das Modell den ersten Entwurf des Angebotsschreibens. Es nutzt dabei archivierte, erfolgreiche Angebote der Vergangenheit als Referenzstil („Few-Shot Prompting“), übernimmt die Corporate Identity und kalkuliert Standardpositionen vor. 

Der Vertriebsmitarbeiter erhält einen zu 85 Prozent fertigen Entwurf. Seine Aufgabe reduziert sich auf die finale Plausibilitätsprüfung, strategische Preisfeinjustierung und die persönliche Freigabe.

#### Das betriebswirtschaftliche Ergebnis
In der Praxis senkt dieser Workflow die Durchlaufzeit von der Anfrage bis zum fertigen Angebot von durchschnittlich 4 Werktagen auf unter 4 Stunden. Die Konsequenz: Eine messbar höhere Abschlussquote, da Schnelligkeit im modernen B2B-Geschäft oft den Ausschlag gibt, gepaart mit einer spürbaren Entlastung des Vertriebsinnendienstes.

*(Wortanzahl: ca. 450 Wörter)*

---

## 3. Verkaufspreis-Vorschlag & Vertriebsplattform

### Preismodell (B2B-Positionierung)
* **Regulärer Verkaufspreis:** **69,00 € netto** (ca. 82,11 € inkl. 19 % MwSt.)
* **Begründung:** Reine Endverbraucher-E-Books für 9,99 € wirken im Mittelstand unprofessionell und generieren zu geringen Deckungsbeitrag. 69,00 € liegt innerhalb der typischen Kreditkarten-/Spesenfreigabe von Abteilungsleitern ohne formellen Freigabeprozess („No-Brainer-Budget“).

### Empfohlene Verkaufsplattform
* **Plattform:** **Ablefy (ehemals Elopage)** oder **Digistore24** mit eigenem Domain-Branding (alternativ: nativer Shopify/WooCommerce-Checkout mit Stripe).
* **Begründung für Ablefy/Digistore24:**
  * Vollautomatischer Reseller-Vertrag (Übernahme der steuerlichen Haftung/MOSS-Verfahren für EU-Käufe).
  * DSGVO-konforme B2B-Rechnungserstellung inklusive Pflichtangabe von Firmenname und USt-IdNr.
  * Integrierte 1-Click-Upsell-Infrastruktur für Folgeprodukte.

---

## 4. Upsell-Produkt: Kurs-Gliederung (5 Module)

### Kurstitel
**Implementierungs-Masterclass: Der 6-Wochen-KI-Sprint für KMU-Führungskräfte**  
*(Preisvorschlag: 790,00 € netto als Self-Paced-Videokurs inklusive Vorlagen und wöchentlichem Q&A-Call)*

* **Modul 1: Architektur, Tool-Setup & Governance**
  * Auswahl des richtigen LLM-Providers (Azure OpenAI vs. ChatGPT Enterprise vs. Open Source).
  * DSGVO-konforme Auftragsverarbeitungsverträge (AVV) und Erstellung von internen KI-Betriebsvereinbarungen.
  * Rollen- und Rechtematrix für den Mittelstand.

* **Modul 2: No-Code-Automatisierung mit Make.com & Webhooks**
  * Grundlagen von APIs und Schnittstellen ohne Programmierkenntnisse.
  * Schritt-für-Schritt-Aufbau von Datenpipelines: E-Mail-Eingang -> LLM -> CRM / ERP.
  * Fehlerbehandlung und Monitoring von automatisierten Prozessen.

* **Modul 3: Das interne Firmen-Gehirn (Wissensmanagement & RAG)**
  * Strukturierung interner Daten (Handbücher, SOPs, QM-Dokumente).
  * DSGVO-konformer Aufbau einer Vektordatenbank / Embedding-Suche.
  * Bereitstellung eines internen Fach-Chatbots für Service und Produktion.

* **Modul 4: Operative Vertriebs- und Marketing-Automatisierung**
  * Live-Implementierung des Vorqualifizierungs- und Angebotsworkflows aus Kapitel 5.
  * Personalisierte B2B-Kampagnenführung mit dynamischen Inhalten.
  * Automatisierte Wettbewerbs- und Marktrecherchen auf Knopfdruck.

* **Modul 5: Change Management, Rollout & ROI-Controlling**
  * Qualifizierung der Mitarbeiter: Prompts schreiben für Nicht-Techniker.
  * Definition und Messung von Key Performance Indicators (KPIs) für Automatisierungsgewinne.
  * Kontinuierliche Prozessoptimierung und Skalierung im Unternehmen.
