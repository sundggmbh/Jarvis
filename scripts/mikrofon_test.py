import sys

try:
    import pyaudio
except ImportError:
    try:
        import pyaudiowpatch
        sys.modules["pyaudio"] = pyaudiowpatch
        import pyaudio
    except ImportError:
        print("FEHLER: Kein Mikrofon-Paket gefunden.")
        print("Nachinstallieren mit: pip install PyAudioWPatch")
        sys.exit(1)

try:
    import speech_recognition as sr
except ImportError:
    print("FEHLER: SpeechRecognition ist nicht installiert.")
    print("Nachinstallieren mit: pip install SpeechRecognition PyAudioWPatch")
    sys.exit(1)


def eingabegeraete(p):
    gesehene = set()
    for index in range(p.get_device_count()):
        info = p.get_device_info_by_index(index)
        if info.get("maxInputChannels", 0) > 0 and info["name"] not in gesehene:
            gesehene.add(info["name"])
            yield index, info["name"]


def aufnahme_level(p, index, dauer=3.0, rate=16000):
    try:
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, input_device_index=index, frames_per_buffer=1024)
        werte = []
        for _ in range(int(rate / 1024 * dauer)):
            daten = stream.read(1024, exception_on_overflow=False)
            stueck = list(daten)
            summe = sum(abs(x) for x in stueck[::16])
            werte.append(summe / (len(stueck[::16]) or 1))
        stream.stop_stream()
        stream.close()
        return sum(werte) / len(werte) if werte else 0
    except Exception as e:
        print(f"    (Gerät {index} konnte nicht geöffnet werden: {type(e).__name__})")
        return -1


def main():
    print("=== MIKROFON-TEST 2 ===")
    print()
    p = pyaudio.PyAudio()
    geräte = list(eingabegeraete(p))
    print(f"Gefundene Eingabegeraete: {len(geräte)}")
    print()
    print("Sprich JETZT die ganze Zeit (ca. 3 Sekunden pro Geraet):")
    print("Sag immer wieder: 'Hallo Jarvis, kannst du mich hoeren?'")
    print()
    ergebnisse = []
    for index, name in geräte:
        print(f"  Teste [{index}] {name} ...", flush=True)
        level = aufnahme_level(p, index)
        if level >= 0:
            print(f"    Pegel: {level:.0f}")
            ergebnisse.append((level, index, name))
    p.terminate()
    print()
    if not ergebnisse:
        print("Kein Geraet liefert Ton. Pruefe: Windows-Einstellungen -> System -> Sound -> Eingabe.")
        sys.exit(1)
    ergebnisse.sort(reverse=True)
    bester_level, bester_index, bester_name = ergebnisse[0]
    print(f"Bester Kandidat: [{bester_index}] {bester_name} (Pegel {bester_level:.0f})")
    print()
    if bester_level < 5:
        print("Alle Geraete sind praktisch stumm. Moegliche Ursachen:")
        print("  1) Mikrofon ist stummgeschaltet (Taste am Laptop oder Sound-Einstellungen)")
        print("  2) Windows-Einstellungen -> Datenschutz und Sicherheit -> Mikrofon ->")
        print("     'Desktop-Apps zulassen' muss EIN sein")
        sys.exit(1)

    print("Schritt 2: Spracherkennung mit dem besten Geraet (braucht Internet):")
    print("SAG JETZT ETWAS (5 Sekunden) ...")
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone(device_index=bester_index) as quelle:
            recognizer.adjust_for_ambient_noise(quelle, duration=1)
            audio = recognizer.listen(quelle, timeout=5, phrase_time_limit=8)
        text = recognizer.recognize_google(audio, language="de-DE")
        print(f"  ERKANNT: {text}")
        print()
        print("=== ALLES FUNKTIONIERT! ===")
        print(f"Dein Jarvis-Mikrofon ist Geraet-Nummer {bester_index} ({bester_name}).")
    except sr.UnknownValueError:
        print("  Ton kam an, aber keine Sprache erkannt - naeher ran und lauter sprechen.")
    except sr.RequestError as e:
        print(f"  Erkennungsdienst nicht erreichbar: {e}")
        print("  Die Erkennung braucht Internet.")
    except Exception as e:
        print(f"  FEHLER: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
