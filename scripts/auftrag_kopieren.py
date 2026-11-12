import sys
import webbrowser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.rollen import STANDARD_AUFTRAG  # noqa: E402

GITHUB_SEITE = "https://github.com/sundggmbh/Jarvis/actions/workflows/agentennetzwerk.yml"

AUFTRAEGE = {
    "1": (
        "Bretten-Recherche",
        "Recherchiere die Geschäftsidee: Aufbau und Verkauf lokaler KI-Agentennetzwerke für kleine und mittlere Betriebe (Handwerk, Arztpraxen, Kanzleien, Einzelhandel) in der Region Bretten / Landkreis Karlsruhe (Kraichgau, Baden-Württemberg). Prüfe: 1) Markt und Wettbewerber, 2) Preisgestaltung (einmalige Einrichtung + monatliche Wartung), 3) Datenschutz/DSGVO-Anforderungen, 4) Wer wäre der erste Pilotkunde in der Region?, 5) Risiken.",
    ),
    "2": (
        "Micro-Audit-Angebot",
        "Entwickle das Angebot \"Micro-Audit für Betriebs-Websites\" der GmbH komplett aus: 1) Erstelle eine Preisliste mit 3 Paketen (Basis-Prüfung 290 €, Plus-Prüfung mit DSGVO und Barrierefreiheit 490 €, Komplett-Prüfung mit Handlungsempfehlungen 750 €) und beschreibe genau, was der Kunde in jedem Paket bekommt. 2) Schreibe einen freundlichen Ansprache-Text (max. 150 Wörter) für die erste E-Mail an Handwerksbetriebe, Arztpraxen und Kanzleien in der Region Bretten / Landkreis Karlsruhe – ohne Fachwörter, ohne Druck, mit klarem Nutzen. 3) Erstelle eine Checkliste mit 15 konkreten Prüfpunkten, die die Agenten bei jeder Website automatisch durchgehen (Technik, Datenschutz, Barrierefreiheit, Textqualität, Kontaktdaten, Impressum). 4) Entwirf den Ablauf von der Anfrage bis zur Rechnung (Ziel: unter 4 Stunden). 5) Plane die ersten 3 Pilotkunden zum Sonderpreis von 250 € gegen ein Empfehlungsschreiben: Wo findet man sie, wie spricht man sie an? 6) Liste die rechtlichen Pflichten (Impressum, Datenschutzerklärung, AGB-Haftungshinweis), die die GmbH selbst auf der Angebots-Seite braucht.",
    ),
    "3": ("Standardauftrag", STANDARD_AUFTRAG),
}

ALLE = "4"


def kopieren(text: str) -> None:
    import tkinter as tk

    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()


def menue_zeigen() -> None:
    print("Welchen Auftrag sollen die Agenten bekommen?")
    for taste, (name, _) in AUFTRAEGE.items():
        print(f"  [{taste}] {name}")
    print(f"  [{ALLE}] ALLE DREI nacheinander starten")


def eine_starten(taste: str, nummer: int = 1) -> None:
    name, text = AUFTRAEGE[taste]
    kopieren(text)
    print(f"\n{nummer}. Auftrag '{name}' ist kopiert ({len(text)} Zeichen).")
    print("   Jetzt im Browser:")
    print(f"   1) Diese Seite oeffnen: {GITHUB_SEITE}")
    print("   2) 'Run workflow' klicken")
    print("   3) Strg+V zum Einfuegen")
    print("   4) Gruenen Knopf 'Run workflow' druecken")
    try:
        webbrowser.open(GITHUB_SEITE)
    except Exception:
        print("   (Seite konnte nicht automatisch geoeffnet werden - Link oben von Hand oeffnen.)")


def alle_starten() -> None:
    for nummer, taste in enumerate(AUFTRAEGE, start=1):
        eine_starten(taste, nummer)
        if nummer < len(AUFTRAEGE):
            input("\nWenn eingefuegt und gestartet: ENTER druecken fuer den naechsten Auftrag ...")
    print("\nAlle Auftraege abgearbeitet - die Agenten arbeiten jetzt der Reihe nach!")


def main() -> None:
    menue_zeigen()
    wahl = input("Nummer eintippen und Enter druecken: ").strip()
    if wahl == ALLE:
        alle_starten()
    elif wahl in AUFTRAEGE:
        eine_starten(wahl)
    else:
        print("Unbekannte Nummer - nichts kopiert.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
