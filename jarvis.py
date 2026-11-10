import pyttsx3
import subprocess
from datetime import datetime

def sprich(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def terminal_befehl(befehl):
    try:
        ergebnis = subprocess.run(befehl, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        ausgabe = ergebnis.stdout.strip()
        if ergebnis.stderr.strip():
            ausgabe += "\nFehler: " + ergebnis.stderr.strip()
        return ausgabe if ausgabe else "(Befehl ausgeführt, keine Ausgabe)"
    except Exception as e:
        return f"Fehler: {e}"

def verarbeite(befehl):
    befehl = befehl.lower().strip()
    if not befehl:
        return True

    if "hallo" in befehl or "jarvis" in befehl:
        sprich("Hallo! Ich bin Jarvis. Wie kann ich helfen?")
        print("🤖 Hallo! Ich bin Jarvis. Wie kann ich helfen?")

    elif "beenden" in befehl or "tschüss" in befehl or "auf wiedersehen" in befehl:
        sprich("Auf Wiedersehen! Bis zum nächsten Mal.")
        print("👋 Auf Wiedersehen!")
        return False

    elif "zeit" in befehl:
        jetzt = datetime.now().strftime("%H:%M Uhr")
        sprich(f"Es ist jetzt {jetzt}.")
        print(f"🕐 Es ist jetzt {jetzt}.")

    elif "zittau" in befehl:
        sprich("Zittau ist ein Luftkurort in Sachsen.")
        print("🏔️ Zittau ist ein Luftkurort in Sachsen.")

    elif "westpark" in befehl:
        sprich("Das Westpark Center ist einer der größten Indoor- und Outdoor-Spielplätze in Sachsen.")
        print("🎪 Das Westpark Center ist einer der größten Indoor- und Outdoor-Spielplätze in Sachsen.")

    elif "terminal" in befehl or "befehl" in befehl:
        sprich("Welchen Befehl soll ich ausführen?")
        cmd = input("⌨️ Befehl eingeben: ")
        if cmd:
            ergebnis = terminal_befehl(cmd)
            print("🖥️ Ausgabe:", ergebnis)
            sprich("Der Befehl wurde ausgeführt.")

    else:
        sprich("Ich habe den Befehl nicht verstanden.")
        print("❓ Befehl nicht erkannt. Versuche: hallo, zeit, zittau, westpark, terminal, beenden")

    return True

if __name__ == "__main__":
    sprich("Jarvis ist bereit.")
    print("🤖 Jarvis ist bereit. Tippe deine Befehle ein (oder 'beenden' zum Schluss).")
    while True:
        texte = input("\n> ")
        if not verarbeite(texte):
            break