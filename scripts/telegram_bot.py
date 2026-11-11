import os
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.rollen import STANDARD_AUFTRAG  # noqa: E402

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "sundggmbh/Jarvis")
WORKFLOW = "agentennetzwerk.yml"


def _github_token() -> str:
    return os.environ.get("GITHUB_TOKEN", "")

HILFE = (
    "Jarvis-Netzwerk Fernsteuerung\n\n"
    "/status - Zeigt, ob die Agenten gerade arbeiten\n"
    "/bericht - Startet einen vollen Netzwerk-Lauf (Arbeitsproben + Bericht)\n"
    "/auftrag <Text> - Startet die Agenten mit deinem eigenen Auftrag\n\n"
    "Beispiel: /auftrag Recherchiere Preise fuer KI-Content-Dienstleistungen in Deutschland"
)


def _befehl(text: str) -> tuple[str, str]:
    teile = text.strip().split(maxsplit=1)
    befehl = teile[0].split("@")[0].lower() if teile else ""
    rest = teile[1].strip() if len(teile) > 1 else ""
    return befehl, rest


def _letzte_run_infos(daten: dict) -> list[str]:
    runs = daten.get("workflow_runs", [])
    if not runs:
        return ["Noch keine Laeufe vorhanden."]
    zeilen = []
    for run in runs[:3]:
        emoji = {"success": "OK", "failure": "FEHLER", "in_progress": "LAEUFT", "queued": "WARTET", "pending": "WARTET"}.get(
            run.get("conclusion") or run.get("status"), "?"
        )
        zeilen.append(f"{emoji} #{run.get('run_number')} ({run.get('created_at', '')[:16]} UTC)")
    return zeilen


async def _status() -> str:
    async with httpx.AsyncClient(timeout=30) as client:
        antwort = await client.get(
            f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/{WORKFLOW}/runs",
            params={"per_page": 3},
            headers={"Authorization": f"Bearer {_github_token()}"},
        )
        antwort.raise_for_status()
        zeilen = _letzte_run_infos(antwort.json())
    return "Letzte Netzwerk-Laeufe:\n" + "\n".join(zeilen)


async def _starten(auftrag: str) -> str:
    if not _github_token():
        return (
            "Fehler: Kein GITHUB_TOKEN gesetzt. Ich kann den Lauf nicht starten. "
            "Siehe README, Abschnitt Telegram."
        )
    async with httpx.AsyncClient(timeout=30) as client:
        antwort = await client.post(
            f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/{WORKFLOW}/dispatches",
            json={"ref": "main", "inputs": {"auftrag": auftrag}},
            headers={
                "Authorization": f"Bearer {_github_token()}",
                "Accept": "application/vnd.github+json",
            },
        )
    if antwort.status_code == 204:
        return (
            "Auftrag an die Agenten uebergeben! Der Lauf dauert ca. 10-15 Minuten.\n"
            "Danach mit /status pruefen, ob er fertig ist."
        )
    return f"Fehler beim Starten (HTTP {antwort.status_code}). Token-Berechtigung pruefen."


async def antwort_auf(text: str) -> str:
    befehl, rest = _befehl(text)
    if befehl in ("/start", "/hilfe", "/help"):
        return HILFE
    if befehl == "/status":
        return await _status()
    if befehl == "/bericht":
        return await _starten(STANDARD_AUFTRAG)
    if befehl == "/auftrag":
        if not rest:
            return "Bitte so: /auftrag <dein Auftrag fuer die Agenten>"
        return await _starten(rest)
    return "Unbekannter Befehl.\n\n" + HILFE


async def _senden(chat_id: int | str, text: str) -> None:
    async with httpx.AsyncClient(timeout=30) as client:
        await client.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text[:4000]},
        )


async def _update_verarbeiten(update: dict) -> None:
    nachricht = update.get("message") or {}
    text = nachricht.get("text", "")
    chat_id = nachricht.get("chat", {}).get("id")
    if not text or chat_id is None:
        return
    try:
        antwort = await antwort_auf(text)
    except Exception as fehler:
        antwort = f"Unerwarteter Fehler: {type(fehler).__name__}"
    await _senden(chat_id, antwort)


async def schleife() -> None:
    if not TELEGRAM_TOKEN:
        raise SystemExit("TELEGRAM_BOT_TOKEN ist nicht gesetzt. Siehe README, Abschnitt Telegram.")
    offset = 0
    print("Jarvis-Telegram-Fernsteuerung laeuft. Zum Beenden Strg+C druecken.")
    async with httpx.AsyncClient(timeout=40) as client:
        while True:
            try:
                antwort = await client.get(
                    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates",
                    params={"timeout": 30, "offset": offset},
                )
                antwort.raise_for_status()
                for update in antwort.json().get("result", []):
                    offset = update["update_id"] + 1
                    await _update_verarbeiten(update)
            except httpx.HTTPError as fehler:
                print(f"Netzwerkfehler, versuche weiter: {type(fehler).__name__}")
                await asyncio_sleep(10)


async def asyncio_sleep(sekunden: float) -> None:
    import asyncio

    await asyncio.sleep(sekunden)


if __name__ == "__main__":
    import asyncio

    asyncio.run(schleife())
