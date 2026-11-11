import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "agentennetzwerk.py"


def _lade_script():
    spec = importlib.util.spec_from_file_location("agentennetzwerk_script", SCRIPT_PATH)
    modul = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modul
    spec.loader.exec_module(modul)
    return modul


def _rolle(name: str):
    from shared.rollen import AgentenRolle

    return AgentenRolle(name=name, beschreibung="Test", auftrag="Testanweisung")


@pytest.fixture()
def script(monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "gemini")
    monkeypatch.setenv("NETZWERK_MIT_SUCHE", "0")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    modul = _lade_script()
    modul._verwendete_backends.clear()
    modul._backend_status["ollama"] = None
    return modul


async def test_gemini_backend_wird_genutzt(script, monkeypatch):
    async def fake(system, nutzer):
        return "Gemini-Antwort"

    monkeypatch.setattr(script, "_gemini_chat", fake)
    text = await script.frage_agent(_rolle("marktchancen-agent"), "hallo")
    assert text == "Gemini-Antwort"
    assert script._verwendete_backends["marktchancen-agent"] == "gemini"


async def test_ollama_backend_wird_genutzt(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "ollama")
    modul = _lade_script()
    modul._verwendete_backends.clear()
    modul._backend_status["ollama"] = None

    async def fake(system, nutzer):
        return "Ollama-Antwort"

    monkeypatch.setattr(modul, "_ollama_chat", fake)
    text = await modul.frage_agent(_rolle("content-agent"), "hallo")
    assert text == "Ollama-Antwort"
    assert modul._verwendete_backends["content-agent"] == "ollama"


async def test_hybrid_teilt_agenten_auf_beide_backends(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "hybrid")
    modul = _lade_script()
    modul._verwendete_backends.clear()
    modul._backend_status["ollama"] = True

    gemini_namen = []
    ollama_namen = []

    async def fake_gemini(system, nutzer):
        gemini_namen.append(system)
        return "g"

    async def fake_ollama(system, nutzer):
        ollama_namen.append(system)
        return "o"

    monkeypatch.setattr(modul, "_gemini_chat", fake_gemini)
    monkeypatch.setattr(modul, "_ollama_chat", fake_ollama)

    for name in modul._bekannte_namen:
        await modul.frage_agent(_rolle(name), "hallo")

    assert gemini_namen and ollama_namen
    assert len(gemini_namen) + len(ollama_namen) == len(modul._bekannte_namen)
    verteilung = set(modul._verwendete_backends.values())
    assert verteilung == {"gemini", "ollama"}


async def test_fallback_gemini_zu_ollama(script, monkeypatch):
    script._backend_status["ollama"] = True

    async def kaputt(system, nutzer):
        raise RuntimeError("Gemini nicht erreichbar")

    async def ok(system, nutzer):
        return "Ollama-Ersatz"

    monkeypatch.setattr(script, "_gemini_chat", kaputt)
    monkeypatch.setattr(script, "_ollama_chat", ok)
    text = await script.frage_agent(_rolle("marktchancen-agent"), "hallo")
    assert text == "Ollama-Ersatz"
    assert script._verwendete_backends["marktchancen-agent"] == "ollama"


async def test_fallback_ollama_zu_gemini(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "ollama")
    modul = _lade_script()
    modul._verwendete_backends.clear()
    modul._backend_status["ollama"] = None

    async def kaputt(system, nutzer):
        raise RuntimeError("Ollama laeuft nicht")

    async def ok(system, nutzer):
        return "Gemini-Ersatz"

    monkeypatch.setattr(modul, "_ollama_chat", kaputt)
    monkeypatch.setattr(modul, "_gemini_chat", ok)
    text = await modul.frage_agent(_rolle("content-agent"), "hallo")
    assert text == "Gemini-Ersatz"
    assert modul._verwendete_backends["content-agent"] == "gemini"


async def test_beide_backends_fehlgeschlagen(script, monkeypatch):
    script._backend_status["ollama"] = True

    async def kaputt(system, nutzer):
        raise RuntimeError("Ausfall")

    monkeypatch.setattr(script, "_gemini_chat", kaputt)
    monkeypatch.setattr(script, "_ollama_chat", kaputt)
    with pytest.raises(RuntimeError):
        await script.frage_agent(_rolle("marktchancen-agent"), "hallo")


async def test_fallback_wird_uebersprungen_wenn_ollama_fehlt(script, monkeypatch):
    script._backend_status["ollama"] = False
    aufrufe = []

    async def kaputt(system, nutzer):
        aufrufe.append("gemini")
        raise RuntimeError("Gemini nicht erreichbar")

    async def nie_gerufen(system, nutzer):
        aufrufe.append("ollama")
        return "sollte nicht passieren"

    monkeypatch.setattr(script, "_gemini_chat", kaputt)
    monkeypatch.setattr(script, "_ollama_chat", nie_gerufen)
    with pytest.raises(RuntimeError):
        await script.frage_agent(_rolle("marktchancen-agent"), "hallo")
    assert aufrufe == ["gemini", "gemini", "gemini"]


async def test_backend_verfuegbar_erkennung(script, monkeypatch):
    class FakeAntwort:
        status_code = 200

    class FakeClient:
        def __init__(self, **kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            return False

        async def get(self, url):
            assert url.endswith("/api/tags")
            return FakeAntwort()

    monkeypatch.setattr(script.httpx, "AsyncClient", FakeClient)
    assert await script._backend_verfuegbar("ollama") is True
    assert script._backend_status["ollama"] is True
    assert await script._backend_verfuegbar("gemini") is True


def test_tools_nur_bei_gemini_mit_suche(script, monkeypatch):
    monkeypatch.setattr(script, "MIT_SUCHE", False)
    assert script._tools("gemini") is None
    assert script._tools("ollama") is None

    monkeypatch.setattr(script, "MIT_SUCHE", True)
    tools = script._tools("gemini")
    assert tools is not None and len(tools) == 1
    assert script._tools("ollama") is None


async def test_agent_recherche_ohne_text_fehler(script, monkeypatch):
    async def leer(system, nutzer):
        return "  "

    monkeypatch.setattr(script, "_gemini_chat", leer)
    with pytest.raises(RuntimeError):
        await script.agent_recherche(_rolle("marktchancen-agent"), "auftrag")

    async def voll(system, nutzer):
        return "Ein Befund"

    monkeypatch.setattr(script, "_gemini_chat", voll)
    befund = await script.agent_recherche(_rolle("marktchancen-agent"), "auftrag")
    assert befund.agent == "marktchancen-agent"
    assert befund.befund == "Ein Befund"


async def test_arbeitsproben_landen_im_freigabe_ordner(script, monkeypatch, tmp_path):
    script.AUSGABEN_DIR = tmp_path / "ausgaben"

    async def fake(system, nutzer):
        return "Probe-Inhalt"

    monkeypatch.setattr(script, "_gemini_chat", fake)
    ergebnis = await script.produziere_arbeitsproben(__import__("datetime").datetime(2026, 11, 12))
    assert len(ergebnis) == 5
    for name, pfad in ergebnis:
        assert pfad.parent.name == "2026-11-12"
        assert pfad.read_text(encoding="utf-8").startswith(f"# Arbeitsprobe: {name}")


def test_report_text_enthaelt_backends_und_teile(script, monkeypatch):
    from datetime import datetime, timezone

    from shared.rollen import AgentenBefund

    script._verwendete_backends.clear()
    script._verwendete_backends["marktchancen-agent"] = "gemini"
    script._verwendete_backends["content-agent"] = "ollama"

    befunde = [
        AgentenBefund(agent="marktchancen-agent", befund="Befund Eins"),
        AgentenBefund(agent="content-agent", befund="Befund Zwei"),
    ]
    text = script.report_text("Testauftrag", datetime(2026, 11, 12, tzinfo=timezone.utc), "Konsolidierter Bericht", befunde)
    assert "Backend-Modus:** gemini" in text
    assert "marktchancen-agent: gemini" in text
    assert "content-agent: ollama" in text
    assert "Konsolidierter Bericht" in text
    assert "Befund Eins" in text


def test_agenten_rollen_sind_vollstaendig(script):
    from shared.rollen import AGENTEN_ROLLEN, GESCHAEFTS_AGENTEN

    assert len(AGENTEN_ROLLEN) == 4
    assert len(GESCHAEFTS_AGENTEN) == 5
    namen = {rolle.name for rolle in AGENTEN_ROLLEN + GESCHAEFTS_AGENTEN}
    assert {
        "marktchancen-agent",
        "verdienstmodelle-agent",
        "wettbewerber-agent",
        "risiko-agent",
        "dossier-agent",
        "content-agent",
        "katalog-agent",
        "automatisierungs-agent",
        "akquise-agent",
    } <= namen


async def test_system_anweisung_warnt_ohne_suche(script, monkeypatch):
    rolle = _rolle("marktchancen-agent")
    monkeypatch.setattr(script, "MIT_SUCHE", False)
    assert "keinen Internetzugang" in script._system_anweisung(rolle, "gemini")
    assert "lokal ohne Internetzugang" in script._system_anweisung(rolle, "ollama")

    monkeypatch.setattr(script, "MIT_SUCHE", True)
    assert "keinen Internetzugang" not in script._system_anweisung(rolle, "gemini")
