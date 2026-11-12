import importlib.util
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "jarvis.py"


def _lade_script():
    spec = importlib.util.spec_from_file_location("jarvis_script", SCRIPT_PATH)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def test_jarvis_modul_laedt_ohne_sprachpakete():
    script = _lade_script()
    assert callable(script.verarbeite)
    assert callable(script.hoere)


def test_unbekannte_frage_geht_an_ollama(monkeypatch):
    script = _lade_script()
    antworten = []

    def fake_frage(text):
        antworten.append(text)
        return "Eine kurze Antwort."

    monkeypatch.setattr(script, "frage_ollama", fake_frage)
    assert script.verarbeite("Was ist eine GmbH?") is True
    assert antworten == ["was ist eine gmbh?"]


def test_beenden_stoppt_schleife(monkeypatch):
    script = _lade_script()
    gesprochen = []
    monkeypatch.setattr(script, "sprich", lambda text: gesprochen.append(text))
    assert script.verarbeite("beenden") is False


def test_ollama_antwort_wird_geholt(monkeypatch):
    script = _lade_script()

    class FakeAntwort:
        def raise_for_status(self):
            return None

        def json(self):
            return {"message": {"content": "Hallo, ich bin die lokale Antwort."}}

    monkeypatch.setattr(script.httpx, "post", lambda *args, **kwargs: FakeAntwort())
    assert "lokale Antwort" in script.frage_ollama("Sag hallo")
