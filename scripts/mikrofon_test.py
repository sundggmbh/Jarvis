import sys

try:
    import pyaudio  # noqa: F401
except ImportError:
    try:
        import pyaudiowpatch
        sys.modules["pyaudio"] = pyaudiowpatch
    except ImportError:
        pass

try:
    import speech_recognition as sr
except ImportError:
    print("FEHLER: SpeechRecognition ist nicht installiert.")
    print("Nachinstallieren mit: pip install SpeechRecognition PyAudioWPatch")
    sys.exit(1)

print("=== MIKROFON-TEST ===")
print()

print("Schritt 1: Gefundene Mikrofone:")
namen = sr.Microphone.list_microphone_names()
if not namen:
    print("  KEIN Mikrofon gefunden! Pruefe: Windows-Einstellungen -> Datenschutz -> Mikrofon.")
    sys.exit(1)
for index, name in enumerate(namen):
    print(f"  [{index}] {name}")
print()

print("Schritt 2: Standard-Mikrofon wird geoeffnet ...")
try:
    recognizer = sr.Recognizer()
    mikrofon = sr.Microphone()
    with mikrofon as quelle:
        print("  Mikrofon geoeffnet - OK.")
        recognizer.adjust_for_ambient_noise(quelle, duration=1)
        print(f"  Umgebungsgeraeusch gemessen (Energie: {recognizer.energy_threshold:.0f})")
        print()
        print("Schritt 3: SAG JETZT ETWAS (5 Sekunden Zeit) ...")
        audio = recognizer.listen(quelle, timeout=5, phrase_time_limit=8)
    print("  Aufnahme fertig - OK.")
except Exception as e:
    print(f"  FEHLER beim Mikrofon: {type(e).__name__}: {e}")
    print("  Tipp: Windows-Einstellungen -> Datenschutz und Sicherheit -> Mikrofon ->")
    print("  'Zulassen, dass Desktop-Apps auf Ihr Mikrofon zugreifen' muss EIN sein.")
    sys.exit(1)

print()
print("Schritt 4: Aufnahme wird an die Erkennung geschickt (braucht Internet) ...")
try:
    text = recognizer.recognize_google(audio, language="de-DE")
    print(f"  ERKANNT: {text}")
    print()
    print("=== ALLES FUNKTIONIERT! Jarvis kann dich hoeren. ===")
except sr.UnknownValueError:
    print("  Mikrofon nimmt auf, aber es wurde keine verstaendliche Sprache erkannt.")
    print("  Tipp: Naeher ans Mikrofon, lauter sprechen, ruhiger Raum.")
except sr.RequestError as e:
    print(f"  FEHLER beim Erkennungsdienst: {e}")
    print("  Tipp: Dafuer braucht Jarvis Internet. Ohne Internet erkennt er nichts.")
except Exception as e:
    print(f"  UNBEKANNTER FEHLER: {type(e).__name__}: {e}")
