import asyncio
import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

spec = importlib.util.spec_from_file_location(
    "agentennetzwerk_script", REPO_ROOT / "scripts" / "agentennetzwerk.py"
)
script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(script)

from shared.rollen import AGENTEN_ROLLEN, GESCHAEFTS_AGENTEN, STANDARD_AUFTRAG, AgentenBefund  # noqa: E402


def _rolle(name: str = "test-agent") -> script.AgentenRolle:
    return script.AgentenRolle(name=name, beschreibung="Test", auftrag="Testanweisung")


async def test_frage_agent_nutzt_gemini_backend(monkeypatch):
    monkeypatch.setattr(script, "BACKEND", "gemini")
    aufgerufen = {}

    async def fake_gemini(system, nutzer):
        aufgerufen["system"] = system
        return "Gemini-Antwort"

    monkeypatch.setattr(script, "_gemini_chat", fake_gemini)
    assert await script.frage_agent(_rolle(), "Frage") == "Gemini-Antwort"
    assert "keinen Internetzugang" in aufgerufen["system"]


async def test_frage_agent_nutzt_ollama_backend(monkeypatch):
    monkeypatch.setattr(script, "BACKEND", "ollama")
    aufgerufen = {}

    async def fake_ollama(system, nutzer):
        aufgerufen["system"] = system
        return "Lokale Antwort"

    monkeypatch.setattr(script, "_ollama_chat", fake_ollama)
    assert await script.frage_agent(_rolle(), "Frage") == "Lokale Antwort"
    assert "lokal ohne Internetzugang" in aufgerufen["system"]
    assert aufgerufen["system"].endswith("Testanweisung")


def test_tools_nur_bei_gemini_mit_suche(monkeypatch):
    monkeypatch.setattr(script, "BACKEND", "gemini")
    monkeypatch.setattr(script, "MIT_SUCHE", False)
    assert script._tools() is None

    monkeypatch.setattr(script, "MIT_SUCHE", True)
    assert script._tools() is not None

    monkeypatch.setattr(script, "BACKEND", "ollama")
    assert script._tools() is None


async def test_agent_recherche_ohne_text_fehler(monkeypatch):
    async def fake_leer(rolle, nutzer):
        return "  "

    monkeypatch.setattr(script, "frage_agent", fake_leer)
    try:
        await script.agent_recherche(None, _rolle(), "Auftrag")
        raise AssertionError("RuntimeError erwartet")
    except RuntimeError:
        pass


async def test_arbeitsproben_landen_im_freigabe_ordner(monkeypatch, tmp_path):
    monkeypatch.setattr(script, "AUSGABEN_DIR", tmp_path / "ausgaben")

    async def fake_probe(rolle, nutzer):
        return f"Probe von {rolle.name}"

    monkeypatch.setattr(script, "frage_agent", fake_probe)
    zeitstempel = datetime(2026, 11, 11, 12, 0, tzinfo=timezone.utc)
    proben = await script.produziere_arbeitsproben(zeitstempel)

    assert len(proben) == len(GESCHAEFTS_AGENTEN)
    for name, pfad in proben:
        assert pfad.exists()
        assert f"Probe von {name}" in pfad.read_text(encoding="utf-8")


async def test_alle_geschaefts_agenten_laufen_parallel(monkeypatch):
    monkeypatch.setattr(script, "AUSGABEN_DIR", REPO_ROOT / "ausgaben-test-tmp")

    async def fake_probe(rolle, nutzer):
        await asyncio.sleep(0)
        return "x"

    monkeypatch.setattr(script, "frage_agent", fake_probe)
    proben = await script.produziere_arbeitsproben(datetime(2026, 11, 11, tzinfo=timezone.utc))
    assert {name for name, _ in proben} == {rolle.name for rolle in GESCHAEFTS_AGENTEN}


def test_report_text_enthaelt_alle_teile():
    zeitstempel = datetime(2026, 11, 11, 12, 0, tzinfo=timezone.utc)
    befunde = [AgentenBefund(agent="test-agent", befund="Ein Befund")]
    text = script.report_text(STANDARD_AUFTRAG, zeitstempel, "## Zusammenfassung\nInhalt", befunde)
    assert "# Jarvis Netzwerk-Bericht (2026-11-11 12:00 UTC)" in text
    assert "test-agent" in text
    assert "Ein Befund" in text
    assert "## Zusammenfassung" in text


def test_agenten_rollen_sind_vollstaendig():
    assert len(AGENTEN_ROLLEN) == 4
    assert len(GESCHAEFTS_AGENTEN) == 5
    alle = [r.name for r in AGENTEN_ROLLEN + GESCHAEFTS_AGENTEN]
    assert len(alle) == len(set(alle))
