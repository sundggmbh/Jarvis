import os
import subprocess
import sys
from datetime import datetime

try:
    import pyaudio  # noqa: F401
except ImportError:
    try:
        import pyaudiowpatch
        sys.modules["pyaudio"] = pyaudiowpatch
    except ImportError:
        pass

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

try:
    import speech_recognition
except ImportError:
    speech_recognition = None

try:
    import httpx
except ImportError:
    httpx = None

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODELL = os.environ.get("OLLAMA_MODELL", "llama3.2:3b")


def sprich(text):
    print("🤖 " + text)
    if pyttsx3 is None:
        return
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass


def terminal_befehl(befehl):
    try:
        ergebnis = subprocess.run(befehl, shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        ausgabe = ergebnis.stdout.strip()
        if ergebnis.stderr.strip():
            ausgabe += "\nFehler: " + ergebnis.stderr.strip()
        return ausgabe if ausgabe else "(Befehl ausgeführt, keine Ausgabe)"
    except Exception as e:
        return f"Fehler: {e}"


def frage_ollama(text):
    if httpx is None:
        return "Ich kann die lokale Antwortmaschine nicht erreichen, weil das Paket httpx fehlt."
    try:
        antwort = httpx.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": OLLAMA_MODELL,
                "messages": [
                    {"role": "system", "content": "Du bist Jarvis, der Assistent der GmbH. Antworte kurz, freundlich und auf Deutsch."},
                    {"role": "user", "content": text},
                ],
                "stream": False,
            },
            timeout=300,
        )
        antwort.raise_for_status()
        inhalt = antwort.json()["message"]["content"].strip()
        return inhalt or "Ich habe leider keine Antwort gefunden."
    except Exception as e:
        return f"Ich komme gerade nicht an die lokale Antwortmaschine: {type(e).__name__}. Läuft Ollama?"


def hoere():
    if speech_recognition is None:
        return None
    try:
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as quelle:
            recognizer.adjust_for_ambient_noise(quelle, duration=0.5)
            audio = recognizer.listen(quelle, timeout=6, phrase_time_limit=15)
        return recognizer.recognize_google(audio, language="de-DE")
    except speech_recognition.WaitTimeoutError:
        return ""
    except speech_recognition.UnknownValueError:
        return ""
    except Exception:
        return ""


def verarbeite(befehl):
    befehl = befehl.lower().strip()
    if not befehl:
        return True

    if "beenden" in befehl or "tschüss" in befehl or "auf wiedersehen" in befehl:
        sprich("Auf Wiedersehen! Bis zum nächsten Mal.")
        return False

    if "hallo" in befehl or "jarvis" in befehl:
        sprich("Hallo! Ich bin Jarvis. Frag mich einfach etwas!")

    elif "zeit" in befehl or "uhrzeit" in befehl:
        jetzt = datetime.now().strftime("%H:%M Uhr")
        sprich(f"Es ist jetzt {jetzt}.")

    elif "zittau" in befehl:
        sprich("Zittau ist ein Luftkurort in Sachsen.")

    elif "westpark" in befehl:
        sprich("Das Westpark Center ist einer der größten Indoor- und Outdoor-Spielplätze in Sachsen.")

    elif "terminal" in befehl or "befehl" in befehl:
        sprich("Welchen Befehl soll ich ausführen?")
        cmd = input("⌨️ Befehl eingeben: ")
        if cmd:
            ergebnis = terminal_befehl(cmd)
            print("🖥️ Ausgabe:", ergebnis[:2000])
            sprich("Der Befehl wurde ausgeführt.")

    else:
        sprich(frage_ollama(befehl))

    return True


def schleife_mit_mikrofon():
    sprich("Jarvis ist bereit. Sprich einfach mit mir - sage 'beenden' zum Schluss.")
    while True:
        text = hoere()
        if text is None:
            sprich("Mein Mikrofon-Paket fehlt. Ich schalte auf Tippen um.")
            return schleife_mit_tastatur()
        if not text:
            continue
        print(f"🎤 Du: {text}")
        if not verarbeite(text):
            return


def schleife_mit_tastatur():
    print("🤖 Jarvis ist bereit. Tippe deine Befehle ein (oder 'beenden' zum Schluss).")
    while True:
        texte = input("\n> ")
        if not verarbeite(texte):
            return


if __name__ == "__main__":
    if speech_recognition is None:
        print("Hinweis: Spracherkennung nicht installiert - Jarvis lauscht auf Tippen.")
        print("Nachinstallieren mit: pip install SpeechRecognition PyAudioWPatch")
    schleife_mit_mikrofon()
