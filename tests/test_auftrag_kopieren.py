import importlib.util
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "auftrag_kopieren.py"


def _lade_script():
    spec = importlib.util.spec_from_file_location("auftrag_kopieren_script", SCRIPT_PATH)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def test_drei_auftraege_vorhanden():
    script = _lade_script()
    assert set(script.AUFTRAEGE) == {"1", "2", "3"}
    namen = [name for name, _ in script.AUFTRAEGE.values()]
    assert namen == ["Bretten-Recherche", "Micro-Audit-Angebot", "Standardauftrag"]


def test_auftraege_sind_nicht_leer():
    script = _lade_script()
    for name, text in script.AUFTRAEGE.values():
        assert len(text) > 50, f"Auftrag {name} ist zu kurz"
        assert "Bretten" in text or "Agentennetzwerk" in text or name == "Standardauftrag"


def test_github_seite_gesetzt():
    script = _lade_script()
    assert script.GITHUB_SEITE.startswith("https://github.com/sundggmbh/Jarvis")
