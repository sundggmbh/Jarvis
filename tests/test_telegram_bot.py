import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
BOT_PATH = REPO_ROOT / "scripts" / "telegram_bot.py"


def _lade_bot():
    spec = importlib.util.spec_from_file_location("telegram_bot_modul", BOT_PATH)
    modul = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modul
    spec.loader.exec_module(modul)
    return modul


@pytest.fixture()
def bot(monkeypatch):
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    return _lade_bot()


def test_befehl_parsing(bot):
    assert bot._befehl("/status") == ("/status", "")
    assert bot._befehl("/auftrag Recherchiere Preise") == ("/auftrag", "Recherchiere Preise")
    assert bot._befehl("/START@JarvisBot") == ("/start", "")
    assert bot._befehl("") == ("", "")


async def test_hilfe_und_unbekannt(bot):
    hilfe = await bot.antwort_auf("/start")
    assert "/status" in hilfe and "/bericht" in hilfe and "/auftrag" in hilfe
    unbekannt = await bot.antwort_auf("/quatsch")
    assert "Unbekannter Befehl" in unbekannt


async def test_auftrag_ohne_text_wird_abgelehnt(bot):
    antwort = await bot.antwort_auf("/auftrag")
    assert "Bitte so" in antwort


async def test_starten_ohne_token_gibt_fehler(bot):
    antwort = await bot.antwort_auf("/bericht")
    assert "GITHUB_TOKEN" in antwort


async def test_starten_mit_token_ruft_dispatch(bot, monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    aufgerufen = {}

    class FakeAntwort:
        status_code = 204

    class FakeClient:
        def __init__(self, **kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            return False

        async def post(self, url, json=None, headers=None):
            aufgerufen["url"] = url
            aufgerufen["json"] = json
            return FakeAntwort()

    monkeypatch.setattr(bot.httpx, "AsyncClient", FakeClient)
    antwort = await bot.antwort_auf("/auftrag Eigener Auftrag")
    assert "uebergeben" in antwort
    assert aufgerufen["json"]["ref"] == "main"
    assert aufgerufen["json"]["inputs"]["auftrag"] == "Eigener Auftrag"
    assert "dispatches" in aufgerufen["url"]


def test_run_infos_formatierung(bot):
    daten = {
        "workflow_runs": [
            {"run_number": 7, "conclusion": None, "status": "in_progress", "created_at": "2026-11-11T10:38:43Z"},
            {"run_number": 6, "conclusion": "success", "status": "completed", "created_at": "2026-11-11T10:25:24Z"},
        ]
    }
    zeilen = bot._letzte_run_infos(daten)
    assert len(zeilen) == 2
    assert "LAEUFT" in zeilen[0] and "#7" in zeilen[0]
    assert "OK" in zeilen[1] and "#6" in zeilen[1]
