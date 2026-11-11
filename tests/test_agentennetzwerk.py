import asyncio
from unittest.mock import AsyncMock

import pytest
from mistralai.client.models import TextChunk
from mistralai.workflows.testing import create_test_worker

from worker.workflows import agentennetzwerk
from worker.workflows.agentennetzwerk import (
    AGENTEN_ROLLEN,
    AgentenBefund,
    AgentennetzwerkInput,
    AgentennetzwerkWorkflow,
    bericht_konsolidieren,
    agent_recherche,
)


def _fake_runner_run(befund_text: str):
    async def run(agent, inputs, session=None, max_turns=10):
        return [TextChunk(text=befund_text)]

    return AsyncMock(side_effect=run)


@pytest.fixture
def gemockter_runner(monkeypatch):
    mock = _fake_runner_run("Testbefund")
    monkeypatch.setattr(agentennetzwerk.workflows_mistralai.Runner, "run", mock)
    return mock


async def test_agenten_recherche_liefert_befund(gemockter_runner):
    befund = await agent_recherche(AGENTEN_ROLLEN[0], "Testauftrag")
    assert isinstance(befund, AgentenBefund)
    assert befund.agent == "marktchancen-agent"
    assert befund.befund == "Testbefund"
    assert gemockter_runner.await_count == 1


async def test_agent_recherche_ohne_text_fehler(monkeypatch):
    mock = _fake_runner_run("  ")
    monkeypatch.setattr(agentennetzwerk.workflows_mistralai.Runner, "run", mock)
    with pytest.raises(RuntimeError):
        await agent_recherche(AGENTEN_ROLLEN[0], "Testauftrag")


async def test_netzwerk_laeuft_alle_agenten_parallel(gemockter_runner, temporal_env):
    async with create_test_worker(
        temporal_env, [AgentennetzwerkWorkflow], activities=[agent_recherche, bericht_konsolidieren]
    ):
        result = await temporal_env.client.execute_workflow(
            AgentennetzwerkWorkflow.run,
            AgentennetzwerkInput(auftrag="Testauftrag"),
            id="agentennetzwerk-test-1",
            task_queue="test-task-queue",
        )

    assert result["auftrag"] == "Testauftrag"
    assert len(result["einzelbefunde"]) == len(AGENTEN_ROLLEN)
    assert {befund["agent"] for befund in result["einzelbefunde"]} == {
        rolle.name for rolle in AGENTEN_ROLLEN
    }
    assert result["bericht"] == "Testbefund"
    assert gemockter_runner.await_count == len(AGENTEN_ROLLEN) + 1


def test_agenten_rollen_sind_eindeutig():
    namen = [rolle.name for rolle in AGENTEN_ROLLEN]
    assert len(namen) == len(set(namen))
    assert len(namen) >= 4
