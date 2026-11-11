import asyncio
import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

from google.genai import types

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

spec = importlib.util.spec_from_file_location(
    "agentennetzwerk_script", REPO_ROOT / "scripts" / "agentennetzwerk.py"
)
script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(script)

from shared.rollen import AGENTEN_ROLLEN, STANDARD_AUFTRAG, AgentenBefund  # noqa: E402


class FakeAntwort:
    def __init__(self, text: str):
        self.text = text


class FakeModel:
    def __init__(self, text: str):
        self._text = text
        self.calls: list[dict] = []

    async def generate_content(self, **kwargs):
        self.calls.append(kwargs)
        return FakeAntwort(self._text)


class FakeAio:
    def __init__(self, model: FakeModel):
        self.models = model


class FakeClient:
    def __init__(self, text: str):
        self.model = FakeModel(text)
        self.aio = FakeAio(self.model)


async def test_agent_recherche_liefert_befund_mit_websuche():
    client = FakeClient("Recherche-Ergebnis")
    befund = await script.agent_recherche(client, AGENTEN_ROLLEN[0], "Auftrag")
    assert befund.agent == "marktchancen-agent"
    assert befund.befund == "Recherche-Ergebnis"
    config = client.model.calls[0]["config"]
    assert config.system_instruction == AGENTEN_ROLLEN[0].auftrag
    assert any(tool.google_search is not None for tool in config.tools)


async def test_alle_agenten_werden_parallel_gestartet():
    client = FakeClient("Befund")
    befunde = list(
        await asyncio.gather(*(script.agent_recherche(client, rolle, "Auftrag") for rolle in AGENTEN_ROLLEN))
    )
    assert len(befunde) == len(AGENTEN_ROLLEN)
    assert client.model.calls and len(client.model.calls) == len(AGENTEN_ROLLEN)


async def test_bericht_konsolidieren_ohne_websuche():
    client = FakeClient("## Zusammenfassung\nInhalt")
    bericht = await script.bericht_konsolidieren(client, "Auftrag", [AgentenBefund(agent="a", befund="b")])
    assert bericht.startswith("## Zusammenfassung")
    config = client.model.calls[0]["config"]
    assert not config.tools


async def test_agent_recherche_ohne_text_fehler():
    client = FakeClient("  ")
    try:
        await script.agent_recherche(client, AGENTEN_ROLLEN[0], "Auftrag")
        raise AssertionError("RuntimeError erwartet")
    except RuntimeError:
        pass


def test_report_text_enthaelt_alle_teile():
    zeitstempel = datetime(2026, 11, 11, 12, 0, tzinfo=timezone.utc)
    befunde = [AgentenBefund(agent="test-agent", befund="Ein Befund")]
    text = script.report_text(STANDARD_AUFTRAG, zeitstempel, "## Zusammenfassung\nInhalt", befunde)
    assert "# Jarvis Netzwerk-Bericht (2026-11-11 12:00 UTC)" in text
    assert "test-agent" in text
    assert "Ein Befund" in text
    assert "## Zusammenfassung" in text
