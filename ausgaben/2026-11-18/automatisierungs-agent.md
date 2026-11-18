# Arbeitsprobe: automatisierungs-agent

# JARVIS GMBH | WORKFLOW-AUTOMATISIERUNG FÜR DEN MITTELSTAND
**Verkaufs- und Angebotsunterlage: KI-Agenten-Netzwerk**

---

## TEIL 1: ONE-PAGER

# Das Jarvis Agenten-Netzwerk für Ihr Unternehmen
### *Wachstum ohne Personalengpass: Manuelle Routineprozesse eliminieren, Durchlaufzeiten um bis zu 80 % senken.*

KMU stehen vor der gleichen Herausforderung: Qualifizierte Fachkräfte verbringen Stunden mit Dateneingaben, E-Mail-Sortierung und Belegprüfungen. Das **Jarvis Agenten-Netzwerk** schaltet spezialisierte Software- und KI-Agenten zwischen Ihre bestehenden Systeme (ERP, CRM, Mail, DMS), die diese Workflows rund um die Uhr fehlerfrei und autonom abarbeiten – ohne dass Sie Ihre Kernsoftware austauschen müssen.

---

### Ihr messbarer Nutzen

* **Mitarbeiterfokus auf Wertschöpfung:** Befreien Sie Ihr Kernteam von 10–20 Stunden manueller Copy-Paste-Arbeit pro Woche.
* **Reaktionszeit unter 2 Minuten:** Kundenanfragen und Leads werden sofort erfasst, klassifiziert und vorverarbeitet – auch am Wochenende.
* **Fehlerquote gegen Null:** Standardisierte Validierungsregeln verhindern manuelle Tipp- und Übertragungsfehler.
* **Nahtlose Integration:** Wir bauen auf Ihren bestehenden Tools auf (z. B. Microsoft 365, DATEV, HubSpot, Salesforce, Lexoffice, individuelle ERPs via REST-API/Webhooks).

---

### Der strukturierte Ablauf: In 4 Wochen live

```
[Woche 1: Audit & Blueprint] ➔ [Woche 2-3: MVP-Entwicklung] ➔ [Woche 4: Test & Go-Live] ➔ [Fortlaufend: Betrieb]
```

1. **Audit & Blueprint (Woche 1):** Detailanalyse Ihres Engpass-Prozesses. Definition von Schnittstellen, Randfällen (Edge Cases) und Sicherheitsrichtlinien.
2. **Setup & Implementierung (Woche 2–3):** Konfiguration der Agenten-Logik, Prompt-Chains, API-Konnektoren und Fehler-Routinen in einer geschützten Umgebung.
3. **Pilotphase & Freigabe (Woche 4):** "Human-in-the-Loop"-Phase: Die Agenten arbeiten parallel, Ihr Team prüft die Ergebnisse. Feinjustierung und Übergabe in den Live-Betrieb.
4. **Monitoring & Evolution:** Fortlaufende Systemüberwachung, Modellpflege und Anpassung an Schnittstellen-Updates.

---

### Transparentes Investitionsmodell

Keine versteckten Lizenzfallen. Klare Trennung von Setup und laufendem Betrieb:

| Baustein | Investition | Leistungsumfang |
| :--- | :--- | :--- |
| **Einmaliges Setup** | **2.000 – 10.000 €** *(nach Prozessumfang)* | Prozessdesign, Konnektorenbau, Systemintegration, Datenvalidierung, DSGVO-konforme Architektur, Testing & Mitarbeitereinweisung. |
| **Monatlicher Betrieb & Wartung** | **300 – 1.000 € / Monat** *(nach Agentenanzahl)* | 24/7 API- & Uptime-Monitoring, Prompt-Tuning, Fehlerbehandlung bei Formatbrüchen, monatliches Reporting, SLA für Anpassungen. |

*Hinweis: Modellkosten für KI-Endpunkte (z. B. OpenAI, Anthropic oder lokale/europäische Hostings) werden transparent 1:1 nach tatsächlichem Verbrauch über Ihr eigenes Unternehmenskonto abgerechnet (i. d. R. 20–100 €/Monat für typische KMU-Volumen).*

---

## TEIL 2: DREI TYPISCHE AUTOMATISIERUNGS-BAUSTEINE

### Baustein 1: Intelligenter Angebotseingang & Lead-Qualifizierung (Sales-Agent)

* **Das Problem:** Eingehende Anfragen via E-Mail, Kontaktformular oder Portal sind unvollständig, landen im allgemeinen Postfach und bleiben bis zu 48 Stunden unberührt.
* **Die Lösung:** 
  1. *Trigger:* Eingang einer neuen Anfrage.
  2. *Logik:* Der Agent analysiert Freitext, extrahiert Unternehmensdaten, Projektumfang, Budget und Dringlichkeit.
  3. *Anreicherung:* Fehlende Firmendaten werden automatisch über Registerdaten oder LinkedIn abgeglichen.
  4. *Aktion:* Vollständige Anlage des Leads im CRM (z. B. HubSpot, Pipedrive), Zuweisung an den passenden Vertriebsmitarbeiter und Erstellung eines individuellen Antwort-Entwurfs im Postausgang.
* **ROI:** Reaktionszeit sinkt von 24–48 Std. auf < 3 Minuten. Steigerung der Abschlussquote um messbar 15–25 %.

---

### Baustein 2: Eingangsrechnungs-Vorprüfung & ERP-Vorvalidierung (Finance-Agent)

* **Das Problem:** Eingangsrechnungen kommen als PDF per Mail, müssen manuell heruntergeladen, geöffnet, mit Bestellungen abgeglichen und im Buchhaltungssystem abgetippt werden.
* **Die Lösung:**
  1. *Trigger:* Eingang einer Rechnung per Mail oder Scan-Ordner.
  2. *Extraktion:* LLM-basierte Extraktion aller Pflichtangaben nach § 14 UStG (IBAN, Rechnungsnummer, Einzelposten, Steuersätze), unabhängig vom Layout des Dokuments.
  3. *Validierung:* Automatischer Abgleich gegen offene Bestellungen oder Verträge im ERP.
  4. *Routing:* 
     * *Bei Match:* Vorbereitung des Buchungssatzes in DATEV / Lexoffice und Weiterleitung zur 1-Klick-Freigabe an den Budgetverantwortlichen.
     * *Bei Diskrepanz:* Markierung und Weiterleitung an den Einkauf mit präzisem Fehlerhinweis.
* **ROI:** Reduktion der Belegdurchlaufzeit um 75 %, Vermeidung von Skontoverlusten.

---

### Baustein 3: Support- & Ticket-Triage mit Lösungsvorschau (Service-Agent)

* **Das Problem:** Der First-Level-Support verbringt 40 % der Zeit mit Standardfragen („Wo ist meine Lieferung?“, „Passwort-Reset“, „Fehlermeldung X“) und manuellem Tagging im Ticket-System.
* **Die Lösung:**
  1. *Trigger:* Eingang eines Tickets (Zendesk, Freshdesk, E-Mail).
  2. *Klassifizierung:* Sentiment-Erkennung (Verärgerungsgrad), Themenzuordnung und Dringlichkeitseinstufung.
  3. *Wissensabgleich:* Abgleich mit interner Wissensdatenbank (Confluence, Notion, PDF-Handbücher).
  4. *Aktion:* Bei Standardanfragen: Automatischer, hochpräziser Lösungsvorschlag als Entwurf für den Agenten (Human-in-the-Loop) oder bei Routinefällen vollautomatischer Versand. Bei komplexen Fällen: Eskalation an den zuständigen Fachexperten mit Zusammenfassung.
* **ROI:** 40 % Entlastung im First-Level-Support; Tickets werden bereits beim ersten Kontakt zu 60 % schneller gelöst (First Contact Resolution).

---

## TEIL 3: HÄUFIGE EINWÄNDE & SCHLAGFERTIGE ANTWORTEN

#### Einwand 1: „Unsere Daten sind unstrukturiert und unsere Systeme veraltet – das funktioniert bei uns nicht.“
> **Antwort:**  
> *„Genau dafür sind KI-Agenten konzipiert. Frühere Automatisierungswerkzeuge brauchten starre Tabellen. Unsere Agenten verstehen unstrukturierte Freitexte, Scans und chaotische E-Mails genauso wie ein menschlicher Mitarbeiter. Wir setzen auf Ihre vorhandene Software auf – Sie müssen kein neues ERP einführen und keine Daten mühsam bereinigen.“*

#### Einwand 2: „KI halluziniert und macht Fehler. Wir können uns keine falschen Rechnungen oder fehlerhaften Angebote leisten.“
> **Antwort:**  
> *„Vollkommen berechtigt. Deshalb setzen wir auf ein zweistufiges Sicherheitsnetz: Erstens arbeiten unsere Agenten mit deterministischen Validierungsregeln (z. B. mathematischer Querabgleich bei Summen). Zweitens etablieren wir standardmäßig das 'Human-in-the-Loop'-Prinzip: Bei Beträgen über Schwellenwert X oder Unsicherheiten legt der Agent die Aufgabe Ihrem Team zur 1-Klick-Bestätigung vor. Die Kontrolle bleibt zu 100 % bei Ihnen.“*

#### Einwand 3: „Wie steht es um Datenschutz und DSGVO? Gehen unsere Geschäftsdaten an US-Konzerne?“
> **Antwort:**  
> *„Datensicherheit ist das Fundament unseres Setups. Wir nutzen ausschließlich Unternehmens-Schnittstellen (APIs) mit vertraglich garantierter Zero-Data-Retention – Ihre Daten werden nicht zum Trainieren von Modellen verwendet. Auf Wunsch deployen wir Workflows komplett auf Servern innerhalb der EU (z. B. Frankfurt) oder nutzen Open-Source-Modelle in Ihrer eigenen Cloud-Infrastruktur.“*

#### Einwand 4: „Das Setup von bis zu 10.000 € ist uns für ein Experiment zu teuer.“
> **Antwort:**  
> *„Wir machen keine Experimente, sondern berechnen vorab einen klaren Business Case. Ein Mitarbeiter, der 15 Stunden pro Woche manuelle Daten schaufelt, kostet Sie bei moderaten Lohnkosten rund 25.000 bis 30.000 € pro Jahr. Bei einer einmaligen Investition amortisiert sich der Workflow in der Regel bereits nach 3 bis 5 Monaten – ab Monat 6 erwirtschaften Sie damit reine Rendite.“*

---

## TEIL 4: KICKOFF-CHECKLISTE FÜR DEN KUNDEN

Um den ersten Workflow innerhalb von 14 Tagen produktiv zu setzen, benötigen wir vorab folgende Informationen und Zugänge:

### 1. Organisatorisch & Fachlich
- [ ] **Prozessverantwortlicher (SPOC):** 1 fester Ansprechpartner für Rückfragen zu fachlichen Randfällen benannt.
- [ ] **Ist-Prozess-Beschreibung:** Kurze Skizze oder bestehende SOP (Standard Operating Procedure) für den gewählten Baustein.
- [ ] **Testdaten-Set:** 10–20 reale, anonymisierte Beispieldaten vergangener Fälle (z. B. 15 Eingangsrechnungen inkl. Sonderfällen wie Gutschriften oder 15 typische Support-Mails).
- [ ] **Regelwerk & Schwellenwerte:** Definition von Grenzwerten (z. B. „Rechnungen bis 500 € vollautomatisch, darüber Freigabe durch Geschäftsleitung“).

### 2. Technisch & Schnittstellen
- [ ] **System-Inventar:** Auflistung der involvierten Software (Name, Version, Cloud vs. On-Premise).
- [ ] **API-Zugänge / Service-Accounts:**
  - [ ] E-Mail-Postfach (IMAP/SMTP oder Microsoft 365 / Google Workspace Service Principal).
  - [ ] CRM / ERP / Buchhaltung (API-Key mit Lese- und Schreibrechten für die Testumgebung).
- [ ] **Testumgebung (Sandbox):** Zugang zu einem Staging-/Testmandanten (falls im Kernsystem vorhanden).

### 3. Datenschutz & Compliance
- [ ] **AVV (Auftragsverarbeitungsvertrag):** Prüfung und Gegenzeichnung des Jarvis-GmbH-Standard-AVV.
- [ ] **Freigabe Datenklassifizierung:** Bestätigung, welche sensiblen Datenfelder (z. B. Kundennamen, IBAN) maskiert oder verschlüsselt werden müssen.

---
**Jarvis GmbH** – *Wir bauen die digitale Belegschaft für den Mittelstand.*  
Kontakt: automation@jarvis-gmbh.de | Web: www.jarvis-gmbh.de *(Musterangaben)*
