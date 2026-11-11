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

    async def _sofort(_sekunden):
        return None

    monkeypatch.setattr(modul.asyncio, "sleep", _sofort)
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


async def test_hybrid_teilt_agenten_auf_alle_backends(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "hybrid")
    monkeypatch.setattr(script, "CLOUD_API_KEY", "test-key")
    monkeypatch.setattr(script, "CLOUD2_API_KEY", "test-key2")
    modul = _lade_script()
    modul._verwendete_backends.clear()
    modul._backend_status["ollama"] = True

    async def fake_gemini(system, nutzer):
        return "g"

    async def fake_ollama(system, nutzer):
        return "o"

    async def fake_hermes(system, nutzer):
        return "h"

    async def fake_cloud(system, nutzer):
        return "c"

    async def fake_cloud2(system, nutzer):
        return "c2"

    monkeypatch.setattr(modul, "_gemini_chat", fake_gemini)
    monkeypatch.setattr(modul, "_ollama_chat", fake_ollama)
    monkeypatch.setattr(modul, "_hermes_chat", fake_hermes)
    monkeypatch.setattr(modul, "_cloud_chat", fake_cloud)
    monkeypatch.setattr(modul, "_cloud2_chat", fake_cloud2)

    for name in modul._bekannte_namen:
        await modul.frage_agent(_rolle(name), "hallo")

    verteilung = set(modul._verwendete_backends.values())
    assert verteilung == {"gemini", "ollama", "hermes", "cloud", "cloud2"}
    assert len(modul._verwendete_backends) == len(modul._bekannte_namen)


async def test_hermes_backend_wird_genutzt(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "hermes")
    modul = _lade_script()
    modul._verwendete_backends.clear()

    async def fake(system, nutzer):
        return "Hermes-Antwort"

    monkeypatch.setattr(modul, "_hermes_chat", fake)
    text = await modul.frage_agent(_rolle("content-agent"), "hallo")
    assert text == "Hermes-Antwort"
    assert modul._verwendete_backends["content-agent"] == "hermes"


async def test_cloud_backend_wird_genutzt(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "cloud")
    monkeypatch.setattr(script, "CLOUD_API_KEY", "test-key")
    modul = _lade_script()
    modul._verwendete_backends.clear()

    async def fake(system, nutzer):
        return "Cloud-Antwort"

    monkeypatch.setattr(modul, "_cloud_chat", fake)
    text = await modul.frage_agent(_rolle("risiko-agent"), "hallo")
    assert text == "Cloud-Antwort"
    assert modul._verwendete_backends["risiko-agent"] == "cloud"


async def test_cloud2_backend_wird_genutzt(script, monkeypatch):
    monkeypatch.setenv("NETZWERK_BACKEND", "cloud2")
    modul = _lade_script()
    modul._verwendete_backends.clear()

    async def fake(system, nutzer):
        return "Cloud2-Antwort"

    monkeypatch.setattr(modul, "_cloud2_chat", fake)
    text = await modul.frage_agent(_rolle("risiko-agent"), "hallo")
    assert text == "Cloud2-Antwort"
    assert modul._verwendete_backends["risiko-agent"] == "cloud2"


async def test_fallback_gemini_zu_cloud_ohne_ollama(script, monkeypatch):
    script._backend_status["ollama"] = False
    monkeypatch.setattr(script, "CLOUD_API_KEY", "test-key")

    async def kaputt(system, nutzer):
        raise RuntimeError("Gemini nicht erreichbar")

    async def cloud_ok(system, nutzer):
        return "Cloud-Ersatz"

    monkeypatch.setattr(script, "_gemini_chat", kaputt)
    monkeypatch.setattr(script, "_cloud_chat", cloud_ok)
    text = await script.frage_agent(_rolle("marktchancen-agent"), "hallo")
    assert text == "Cloud-Ersatz"
    assert script._verwendete_backends["marktchancen-agent"] == "cloud"


async def test_fallback_kette_bis_hermes(script, monkeypatch):
    script._backend_status["ollama"] = True

    async def kaputt(system, nutzer):
        raise RuntimeError("Ausfall")

    async def hermes_ok(system, nutzer):
        return "Hermes-Ersatz"

    monkeypatch.setattr(script, "_gemini_chat", kaputt)
    monkeypatch.setattr(script, "_ollama_chat", kaputt)
    monkeypatch.setattr(script, "_hermes_chat", hermes_ok)
    text = await script.frage_agent(_rolle("marktchancen-agent"), "hallo")
    assert text == "Hermes-Ersatz"
    assert script._verwendete_backends["marktchancen-agent"] == "hermes"


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


def test_drossel_fehler_erkennung(script):
    assert script._ist_drossel_fehler(RuntimeError("429 RESOURCE_EXHAUSTED"))
    assert script._ist_drossel_fehler(RuntimeError("quota exceeded"))
    assert script._ist_drossel_fehler(RuntimeError("Rate limit reached"))
    assert not script._ist_drossel_fehler(RuntimeError("Verbindung getrennt"))


async def test_beide_backends_fehlgeschlagen(script, monkeypatch):
    script._backend_status["ollama"] = True

    async def kaputt(system, nutzer):
        raise RuntimeError("Ausfall")

    async def kaputt2(system, nutzer):
        raise RuntimeError("Ausfall")

    monkeypatch.setattr(script, "_gemini_chat", kaputt)
    monkeypatch.setattr(script, "_ollama_chat", kaputt)
    monkeypatch.setattr(script, "_hermes_chat", kaputt2)
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
    assert aufrufe == ["gemini", "gemini", "gemini", "gemini"]


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

    monkeypatch.setattr(script, "CLOUD_API_KEY", "")
    assert await script._backend_verfuegbar("cloud") is False
    monkeypatch.setattr(script, "CLOUD_API_KEY", "test-key")
    assert await script._backend_verfuegbar("cloud") is True

    monkeypatch.setattr(script, "CLOUD2_API_KEY", "")
    assert await script._backend_verfuegbar("cloud2") is False
    monkeypatch.setattr(script, "CLOUD2_API_KEY", "test-key2")
    assert await script._backend_verfuegbar("cloud2") is True


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
    assert len(ergebnis) == 10
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

    assert len(AGENTEN_ROLLEN) == 5
    assert len(GESCHAEFTS_AGENTEN) == 10
    namen = {rolle.name for rolle in AGENTEN_ROLLEN + GESCHAEFTS_AGENTEN}
    assert {
        "marktchancen-agent",
        "verdienstmodelle-agent",
        "wettbewerber-agent",
        "risiko-agent",
        "qualitaets-agent",
        "dossier-agent",
        "content-agent",
        "katalog-agent",
        "automatisierungs-agent",
        "akquise-agent",
        "architekt-agent",
        "seo-agent",
        "social-agent",
        "produkt-agent",
        "ausschreibungs-agent",
    } <= namen


async def test_system_anweisung_warnt_ohne_suche(script, monkeypatch):
    rolle = _rolle("marktchancen-agent")
    monkeypatch.setattr(script, "MIT_SUCHE", False)
    assert "keinen Internetzugang" in script._system_anweisung(rolle, "gemini")
    assert "keinen Internetzugang" in script._system_anweisung(rolle, "ollama")
    assert "keinen Internetzugang" in script._system_anweisung(rolle, "hermes")
    assert "keinen Internetzugang" in script._system_anweisung(rolle, "cloud")

    monkeypatch.setattr(script, "MIT_SUCHE", True)
    assert "keinen Internetzugang" not in script._system_anweisung(rolle, "gemini")
