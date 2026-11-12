# Arbeitsprobe: produkt-agent

# Arbeitsprobe: Digitales Informationsprodukt der Jarvis GmbH

---

## 1. E-Book: Titel und Inhaltsverzeichnis

**Arbeitstitel:**  
*KI-Implementierung im Mittelstand: Der 90-Tage-Blueprint für pragmatische Prozessautomatisierung*  
**Untertitel:**  
*Wie mittelständische Unternehmen interne Workflows automatisieren, Fachkräfte entlasten und messbaren ROI erzielen – ohne Millionenbudgets und Beraterschlachten.*

**Zielgruppe:**  
Geschäftsführer (KMU), COOs, Digitalisierungs- und IT-Leiter im deutschsprachigen Mittelstand (50 bis 500 Mitarbeiter).

### Inhaltsverzeichnis
* **Vorwort:** Warum Mittelständler jetzt handeln müssen – aber pragmatisch, nicht hektisch.
* **Kapitel 1: Der Hype-Filter:** Was Generative KI und Prozessautomation heute im Mittelstand real leisten können (und was Marketing-Märchen sind).
* **Kapitel 2: Die Use-Case-Matrix:** Wie Sie die 20 % der Prozesse identifizieren, die 80 % Zeitersparnis bringen.
* **Kapitel 3: Daten, Datenschutz & DSGVO:** Rechtssicherer Einsatz von LLMs und Automation-Tools in DACH.
* **Kapitel 4: Der modulare Tech-Stack:** No-Code/Low-Code (Make, n8n), LLM-APIs und ERP-Schnittstellen pragmatisch orchestrieren.
* **Kapitel 5: Die zwei Königsdisziplinen:** E-Mail-Triage im Kundenservice und automatisierte Angebotserstellung im Vertrieb.
* **Kapitel 6: Mensch & Betriebsrat mitnehmen:** Change-Management für Vorbehalte, Arbeitsplatzsicherheit und Tool-Akzeptanz.
* **Kapitel 7: Der 90-Tage-Rollout-Fahrplan:** Von der 14-tägigen Pilotphase zur stabilen Produktivumgebung.
* **Kapitel 8: Monitoring, Governance & Skalierung:** KPIs, Fehlertoleranzen und die iterative Weiterentwicklung interner Assistenten.
* **Anhang:** Checklisten, DSGVO-Auftragsverarbeitungs-Leitfaden und Vendor-Evaluation-Sheet.

---

## 2. Ausgeschriebenes Muster-Kapitel

### Kapitel 2: Die Use-Case-Matrix: Wie Sie die 20 % der Prozesse identifizieren, die 80 % Zeitersparnis bringen

Ein weit verbreiteter Fehler im Mittelstand besteht darin, KI mit einem "Gießkannen-Prinzip" einzuführen. Es wird eine Handvoll ChatGPT-Team-Lizenzen gekauft, den Mitarbeitern zur freien Verfügung gestellt und nach drei Monaten resigniert festgestellt, dass zwar ein paar Marketingtexte schneller getippt wurden, die Kernprozesse im Unternehmen jedoch unverändert ineffizient laufen. 

Wenn Sie einen messbaren Return on Investment (ROI) erzielen wollen, müssen Sie dort ansetzen, wo Routinearbeiten qualifizierte Fachkräfte blockieren. Wir nutzen hierfür die von Jarvis etablierte **Impact-Effort-Matrix**.

#### Schritt 1: Die Prozess-Inventur
Bitten Sie Ihre Abteilungsleiter (Vertriebsinnendienst, Einkauf, Kundenservice, Buchhaltung), für fünf Arbeitstage alle Aufgaben zu protokollieren, die folgende drei Kriterien erfüllen:
1. **Regelbasierte Struktur:** Der Ablauf folgt klaren Wenn-Dann-Bedingungen (selbst wenn Ausnahmen vorkommen).
2. **Text- oder Datenlastigkeit:** E-Mails, PDFs, Tabellen oder ERP-Eingabemasken sind die primären Medien.
3. **Hohe Frequenz:** Der Prozess wird mindestens 20-mal pro Woche von mehreren Mitarbeitern durchlaufen.

Typische Fundstücke sind: Das manuelle Übertragen von Bestelldaten aus eingehenden PDF-Anhängen in das ERP-System, das Verfassen standardisierter Angebotsbegleitschreiben oder das Vorqualifizieren von Support-Tickets.

#### Schritt 2: Filterung nach Komplexität und Hebel
Tragen Sie die identifizierten Aufgaben in ein Koordinatensystem ein:

* **Horizontale Achse (Implementierungsaufwand):** Wie fragmentiert sind die Daten? Benötigen wir komplexe ERP-Schnittstellen (hoher Aufwand) oder genügen Webhooks und Standard-APIs (geringer Aufwand)?
* **Vertikale Achse (Wirtschaftlicher Hebel):** Wie viele Personenstunden bindet dieser Prozess monatlich multipliziert mit dem Stundensatz der involvierten Mitarbeiter?

Konzentrieren Sie sich im ersten Schritt ausschließlich auf den **oberen linken Quadranten**: Hoher Hebel, geringer bis mittlerer Aufwand.

#### Schritt 3: Der "Human-in-the-Loop"-Grundsatz
Vermeiden Sie bei Ihrem ersten Anwendungsfall Prozesse, die eine vollautonome Entscheidung erfordern. Der größte Hebel für KMU liegt in der **Teilautomatisierung**. 

Ein Praxisbeispiel: Eingehende Ausschreibungsunterlagen werden durch eine Automatisierungsstrecke analysiert. Ein Sprachmodell extrahiert Leistungsdaten, gleicht sie mit Ihrem Standard-Portfolio ab und formuliert einen Angebotsentwurf. Der Vertriebsingenieur muss das Dokument anschließend nicht mehr in 90 Minuten von Grund auf tippen, sondern prüft und korrigiert den Entwurf in 15 Minuten. Die Zeitersparnis beträgt 75 Minuten pro Vorgang – bei null Fehlerrisiko, da die Freigabe weiterhin durch einen Menschen erfolgt.

#### Die Entscheidungsvorlage
Wählen Sie genau **einen** Prozess aus diesem Quadranten für Ihren ersten 30-Tage-Prototyp. Definieren Sie vor Beginn der Umsetzung drei Kennzahlen:
1. Aktuelle Durchlaufzeit pro Vorgang (Ist-Zustand).
2. Ziel-Durchlaufzeit (Soll-Zustand).
3. Akzeptierte Fehlerrate für die maschinelle Vorverarbeitung (Richtwert: unter 5 %).

Erst wenn dieser Pilotprozess stabil läuft und von den Mitarbeitern aktiv genutzt wird, öffnen Sie die Pipeline für den nächsten Use Case.

*(Wortanzahl: ca. 450 Wörter)*

---

## 3. Preispunkt & Plattform-Strategie

| Parameter | Strategische Entscheidung | Begründung |
| :--- | :--- | :--- |
| **Produktpreis** | **89,00 € zzgl. USt.** (E-Book inkl. Vorlagen) | **B2B-Signalwirkung:** Preise unter 30 € wirken auf Entscheider im Mittelstand unseriös und vermitteln "Consumer-Niveau". 89 € ist eine Spesen-Grenze, die Teamleiter ohne formelle Freigabe zeichnen können. |
| **Vertriebsplattform** | **Eigener Shop via Shopify + Stripe** *(Alternativ: Digistore24)* | Volle Kontrolle über Kundendaten, DSGVO-konforme B2B-Rechnungsstellung (inkl. USt-ID-Prüfung) und maximale Marge ohne hohe Marktplatz-Gebühren. Digistore24 eignet sich als Alternative, falls Reseller-Modell für Steuern gewünscht ist. |
| **Order-Bump** | **+ 37,00 € zzgl. USt.** | Vorlagen-Paket: Make.com-Blueprints (.json-Exporte), Betriebsrat-Mustervereinbarung & Prompt-Datenbank. |

---

## 4. Kurs-Gliederung als Upsell-Produkt

**Produkt:**  
*Video-Masterclass: KI-Prozess-Architekt im Mittelstand (Hands-on-Implementierung)*  
**Upsell-Preis:** 890,00 € zzgl. USt. (Selbststudium) bzw. 1.890,00 € (inkl. 2x 1:1 Review-Calls).

### Modulübersicht

* **Modul 1: Architektur & Tool-Evaluation**
  * DSGVO-konforme Cloud-Setups vs. Self-Hosted (Hetzner, Azure Germany, n8n on-premise).
  * API-Grundlagen für Nicht-Entwickler: Authentifizierung, Webhooks und Payload-Handling.

* **Modul 2: No-Code-Automation im Produktiveinsatz**
  * Praxis-Setup: Workflows bauen mit Make oder n8n.
  * Fehlerbehandlung, Fallbacks und Logging (Was passiert, wenn eine Schnittstelle ausfällt?).

* **Modul 3: RAG & Eigene Unternehmensdaten anbinden**
  * Vektor-Datenbanken pragmatisch: Produktdatenblätter und interne Handbücher indexieren.
  * Reduktion von Halluzinationen durch strikte System-Prompts und Guardrails.

* **Modul 4: Die 3 Kern-Pipelines (Live-Bau im Kurs)**
  * *Pipeline A:* E-Mail-Triage & automatisierte Vorsortierung im ERP/CRM.
  * *Pipeline B:* Extrahieren von Bestelldaten aus unstrukturierten Lieferanten-PDFs.
  * *Pipeline C:* KI-gestützte Angebots- und Exposé-Generierung.

* **Modul 5: Governance, Betriebsrat & Skalierung**
  * Betriebsvereinbarung rechtssicher aufsetzen (Musterverträge DACH).
  * Kostenkontrolle bei API-Verbräuchen (Token-Budgetierung und Caching).
  * Übergabe der Systeme an interne Fachabteilungen (Dokumentation & Befähigung).
