import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import AsyncMock

from mistralai.client.models import ConversationResponse, ConversationUsageInfo, MessageOutputEntry, TextChunk

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

spec = importlib.util.spec_from_file_location(
    "agentennetzwerk_script", REPO_ROOT / "scripts" / "agentennetzwerk.py"
)
script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(script)

from shared.rollen import AGENTEN_ROLLEN, STANDARD_AUFTRAG, AgentenBefund  # noqa: E402


def _antwort(text: str) -> ConversationResponse:
    return ConversationResponse(
        conversation_id="conv_1",
        outputs=[MessageOutputEntry(content=[TextChunk(text=text)], role="assistant")],
        usage=ConversationUsageInfo(prompt_tokens=1, completion_tokens=1, total_tokens=2),
    )


async def test_agent_recherche_liefert_befund():
    client = AsyncMock()
    client.beta.conversations.start_async = AsyncMock(return_value=_antwort("Recherche-Ergebnis"))
    befund = await script.agent_recherche(client, AGENTEN_ROLLEN[0], "Auftrag")
    assert befund.agent == "marktchancen-agent"
    assert befund.befund == "Recherche-Ergebnis"
    _, kwargs = client.beta.conversations.start_async.call_args
    assert kwargs["tools"] is not None
    assert kwargs["instructions"] == AGENTEN_ROLLEN[0].auftrag


async def test_alle_agenten_werden_parallel_gestartet():
    client = AsyncMock()
    client.beta.conversations.start_async = AsyncMock(return_value=_antwort("Befund"))
    befunde = await asyncio_gather_alle(client, "Auftrag")
    assert len(befunde) == len(AGENTEN_ROLLEN)
    assert client.beta.conversations.start_async.call_count == len(AGENTEN_ROLLEN)


async def asyncio_gather_alle(client, auftrag):
    return list(
        await __import__("asyncio").gather(
            *(script.agent_recherche(client, rolle, auftrag) for rolle in AGENTEN_ROLLEN)
        )
    )


def test_report_text_enthaelt_alle_teile():
    zeitstempel = datetime(2026, 11, 11, 12, 0, tzinfo=timezone.utc)
    befunde = [AgentenBefund(agent="test-agent", befund="Ein Befund")]
    text = script.report_text(STANDARD_AUFTRAG, zeitstempel, "## Zusammenfassung\nInhalt", befunde)
    assert "# Jarvis Netzwerk-Bericht (2026-11-11 12:00 UTC)" in text
    assert "test-agent" in text
    assert "Ein Befund" in text
    assert "## Zusammenfassung" in text


def test_text_aus_antwort_ignoriert_leeres():
    antwort = _antwort("  ")
    assert script.text_aus_antwort(antwort) == ""
