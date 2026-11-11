# Arbeitsprobe: automatisierungs-agent

# Jarvis GmbH | Angebots- und Leistungspaket
**Intelligente Workflow-Automatisierung für den Mittelstand**

---

## Teil 1: One-Pager – Jarvis Agenten-Netzwerk für Ihr Unternehmen

### Schluss mit manueller Routine: Skalieren ohne zusätzliches Personal
In vielen mittelständischen Unternehmen binden repetitive Datenübertragungen, Dokumentenprüfungen und E-Mail-Routinen wertvolle Fachkräfte. Das **Jarvis Agenten-Netzwerk** schließt die Lücke zwischen isolierten Insellösungen (ERP, CRM, E-Mail, DMS) durch spezialisierte, KI-gestützte Software-Agenten. Diese arbeiten 24/7 im Hintergrund, fehlerfrei und nach Ihren Vorgaben.

---

### Ihr konkreter Nutzen
* **Bis zu 80 % weniger manuelle Routinearbeit:** Fachkräfte gewinnen Zeit für kundennahe Wertschöpfung.
* **Durchlaufzeiten von Minuten statt Tagen:** Schnellere Reaktionszeiten im Vertrieb und Kundenservice.
* **100 % Systemintegration:** Kein Austausch bestehender Software nötig – wir docken an vorhandene APIs oder E-Mail-Schnittstellen an.
* **Volle Kontrolle (Human-in-the-Loop):** Kritische Freigaben verbleiben immer bei Ihren Mitarbeitern.

---

### Der 3-Schritte-Fahrplan zur Einführung

```
[Phase 1: Potenzial-Audit] ──► [Phase 2: Sprint-Implementierung] ──► [Phase 3: Rollout & Betrieb]
      (Woche 1-2)                      (Woche 3-5)                        (Ab Woche 6)
• Prozessanalyse & Prio          • Aufbau & API-Anbindung           • Schulung Ihres Teams
• Definition der Schnittstellen  • Testing mit Realdaten            • 24/7 Monitoring & SLA
• Business-Case & ROI-Kalkulation• Human-in-the-Loop-Testing         • Kontinuierliche Optimierung
```

---

### Investition & Preispakete

Wir bieten transparente Festpreise für die Implementierung kombiniert mit planbaren monatlichen Betriebskosten.

| Leistungsbaustein | **Starter** (1 Prozess) | **Professional** (2–3 Prozesse) | **Enterprise** (End-to-End Netzwerk) |
| :--- | :--- | :--- | :--- |
| **Einmaliges Setup** | **2.000 € – 3.500 €** | **4.500 € – 7.500 €** | **8.000 € – 10.000 €** |
| *Leistung* | 1 Standard-Agent, Anbindung an bis zu 2 Systeme, Basistest. | 2–3 Agenten, komplexe Routinglogik, ERP/CRM-Deep-Integration. | Mehrstufiges Agenten-Netzwerk, Custom-Logik, Legacy-Systemanbindung. |
| **Monatliche Wartung & Ops** | **300 € / Monat** | **550 € / Monat** | **850 € – 1.000 € / Monat** |
| *Inklusive* | API-Monitoring, Fehler-Handling, Plattform-Hosting, 8h SLA. | Laufende Prompt-Optimierung, System-Updates, 4h SLA, Monats-Report. | Proaktives Tuning, Prioritäts-Support, vierteljährlicher Prozess-Review. |

*Alle Preise zzgl. gesetzl. MwSt. Variable Cloud-/Modellkosten (z. B. LLM-Tokens) werden transparent nach Verbrauch weiterberechnet (typischerweise 20–80 €/Monat).*

---

## Teil 2: Drei typische Automatisierungs-Bausteine

### Baustein A: Intelligenter Angebotseingang & Lead-Qualifizierung
* **Problem:** Eingehende Anfragen über Kontaktformulare, Ausschreibungsportale oder Sammelpostfächer bleiben oft Stunden oder Tage liegen. Daten müssen händisch ins CRM eingepflegt werden.
* **Workflow:**
  1. *Eingang:* Jarvis scannt das E-Mail-Postfach auf neue Ausschreibungen oder Leads.
  2. *Extraktion:* Ein LLM-Parser extrahiert Ansprechpartner, Kundennummer, Budget, Leistungsanforderung und Fristen.
  3. *Validierung & Abgleich:* Prüfung gegen das bestehende CRM (z. B. HubSpot, Salesforce, Pipedrive). Existiert der Kontakt bereits?
  4. *Aktion:* Automatisches Anlegen des Deals, Setzen des Fälligkeitsdatums und Erstellung eines vorformulierten Antwortentwurfs für den Vertriebsmitarbeiter.
* **Technologie:** Make/n8n, Python-Worker, strukturierte OpenAI/Anthropic-Extraktion, CRM-REST-APIs.
* **Mehrwert:** Reaktionszeit sinkt auf unter 5 Minuten; Conversion-Rate steigt messbar; null manueller Übertragungsaufwand.

---

### Baustein B: Rechnungs-Vorprüfung & Freigabe-Workflow
* **Problem:** Eingangsrechnungen landen als PDF im E-Mail-Postfach, werden manuell abgetippt, langwierig per Mail zur Freigabe herumgeschickt und verspätet an DATEV/Buchhaltung übergeben.
* **Workflow:**
  1. *PDF-Parsing:* Jarvis liest Rechnungs-PDFs aus, extrahiert IBAN, Rechnungsnummer, USt-IdNr., Brutto-/Nettobeträge sowie Einzelpositionen.
  2. *Bestellabgleich (3-Way-Match):* Automatische Prüfung, ob eine entsprechende Bestellung oder ein Leistungsnachweis vorliegt.
  3. *Freigabe-Ping:* Rechnungszusammenfassung wird per Microsoft Teams / Slack an den zuständigen Projektleiter geschickt (mit 1-Klick-Buttons: „Freigeben“ / „Rückfrage“).
  4. *Übergabe:* Nach Freigabe automatische Übergabe an DATEV Unternehmen online, SevDesk oder Lexware.
* **Technologie:** OCR (z. B. AWS Textract / Azure Document Intelligence), LLM-Validierung, Teams/Slack-Webhooks, Buchhaltungs-Schnittstellen.
* **Mehrwert:** Bis zu 75 % schnellere Durchlaufzeiten; Skonto-Verluste sinken gegen Null; lückenlose Dokumentation für den Wirtschaftsprüfer.

---

### Baustein C: Support-Triage & Vorqualifizierung
* **Problem:** Support-Mitarbeiter verbringen 30–40 % ihrer Zeit damit, Tickets zu kategorisieren, Passwörter zurückzusetzen oder Standardfragen (Lieferstatus, FAQs) abzutippen.
* **Workflow:**
  1. *Eingang & Analyse:* Jarvis analysiert eingehende Tickets (Zendesk, Freshdesk, E-Mail) nach Thema, Dringlichkeit, Sprache und Tonalität (Sentiment Analysis).
  2. *Kategorisierung:* Vergabe von Tags, Zuweisung an die zuständige Fachabteilung (z. B. „Technik Level 2“ vs. „Rechnungswesen“).
  3. *Drafting / Auto-Reply:* Bei Standardfragen (Lieferzeiten, Handbücher) sendet der Agent eine direkte Lösung aus der internen Wissensdatenbank. Bei komplexen Fällen wird eine Antwort für den Agenten vorformuliert.
* **Technologie:** Helpdesk-APIs, Vector-Datenbank (RAG) mit Unternehmens-Wissensbasis, LLM-Routing.
* **Mehrwert:** Sofortige Erstreaktionszeit (First Response Time < 1 Min.); Entlastung des Helpdesks um ca. 40 % des Ticketvolumens.

---

## Teil 3: Einwandbehandlung für Entscheider (FAQ)

### 1. „Datenschutz & DSGVO: Dürfen unsere sensiblen Daten überhaupt an eine KI gesendet werden?“
> **Antwort:** Ja, absolut DSGVO-konform. Wir setzen standardmäßig auf europäische Server-Standorte (z. B. Microsoft Azure Region Frankfurt/Dublin oder AWS Frankfurt) mit strikten Data-Privacy-Agreements (DPA). Die von uns genutzten Enterprise-APIs garantieren vertraglich, dass Ihre Daten **weder gespeichert noch zum Trainieren von Modellen** verwendet werden. Auf Wunsch binden wir vollwertige Open-Source-Modelle (wie Mistral oder Llama) direkt auf Ihrer eigenen Cloud-Infrastruktur oder On-Premises an.

### 2. „Wir sind zu klein, unsere Prozesse sind nicht standardisiert genug.“
> **Antwort:** Genau für diesen Fall eignen sich moderne KI-Agenten. Frühere, starre Automatisierungen (wie Makros) scheiterten an kleinsten Formatänderungen. LLM-basierte Agenten verstehen Kontext und unstrukturierte Daten (z. B. formlose E-Mails, verschiedene Rechnungsformate). Wir beginnen nicht mit einer unternehmensweiten Großbaustelle, sondern isolieren genau **einen** zeitfressenden Prozess mit hohem Standardisierungsgrad.

### 3. „Was passiert, wenn die KI Fehler macht oder halluziniert?“
> **Antwort:** Wir etablieren das Prinzip **„Human-in-the-Loop“**. Jarvis führt kritische Aktionen nicht blind aus, sondern bereitet Entscheidungen vor. Erst wenn Ihr Mitarbeiter auf „Freigeben“ klickt (z. B. direkt in MS Teams oder per Mail), wird der finale Schritt ausgeführt. Zudem sichern deterministische Prüfregeln (z. B. mathematischer Rechnungsabgleich) die KI-Ausgaben ab.

### 4. „Unsere IT-Systeme sind alt und haben keine modernen Schnittstellen.“
> **Antwort:** Wir arbeiten mit hybriden Schnittstellen. Neben modernen REST-APIs nutzen wir SFTP-Datenimporte, automatisierte E-Mail-Parser, Webhooks oder bei Bedarf Headless-Browser-Automatisierung (RPA), um auch ältere ERP- oder Warenwirtschaftssysteme ohne Neuinvestition nahtlos anzubinden.

---

## Teil 4: Kickoff-Checkliste (Onboarding in 10 Arbeitstagen)

Bitte stellen Sie zum Projektstart folgende Unterlagen und Zugänge bereit, um einen reibungslosen Ablauf zu gewährleisten:

### 1. Prozessdokumentation & Fachansprechpartner
- [ ] Benennung eines fachlichen Ansprechpartners (Product Owner intern) mit ca. 2–3 Std. Zeitbudget pro Woche für Abnahmen.
- [ ] Kurzbeschreibung des Zielprozesses (Schritt-für-Schritt, gerne auch als kurze Loom-Videoaufnahme des Bildschirms).
- [ ] Definition der Erfolgskriterien (z. B. „Rechnungen unter 1.000 € ohne Rückfrage in DATEV verbuchen“).

### 2. Testdaten & Edge Cases
- [ ] Mindestens 15–20 reale, anonymisierte Beispieldatensätze (z. B. Rechnungs-PDFs, Support-Mails, Ausschreibungen).
- [ ] Mindestens 3–5 bekannte „Problemfälle / Sonderfälle“ (z. B. ausländische USt-ID, handschriftliche Vermerke, Sammelrechnungen).

### 3. System-Zugänge & Schnittstellen
- [ ] Bereitstellung einer Test- oder Sandbox-Umgebung der Zielsysteme (CRM, ERP, Helpdesk).
- [ ] API-Schlüssel bzw. Admin-Freigaben zur Erstellung von Tokens/Webhooks.
- [ ] Bereitstellung eines dedizierten Service-E-Mail-Accounts (z. B. `jarvis-automation@ihre-domain.de`).

### 4. IT-Sicherheit & Governance
- [ ] Bereitstellung der internen IT-Sicherheits- und Datenschutz-Richtlinien.
- [ ] Unterzeichnung der Auftragsverarbeitungsvereinbarung (AVV) der Jarvis GmbH.
- [ ] Freigabe von Webhooks/IP-Adressen in Ihrer internen Firewall (falls erforderlich).

---
*Erstellt von der Jarvis GmbH. Für Rückfragen oder zur Abstimmung des Kickoff-Termins kontaktieren Sie Ihren Automatisierungs-Agenten.*
