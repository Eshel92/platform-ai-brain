#!/usr/bin/env python3
"""Stop hook: after a long session that saved nothing, ask Claude once whether to save a learning.

Cheap: no model call, it only counts tool calls in the transcript. Fires at most once per session.

Environment:
  BRAIN_DIR              brain clone (default ~/platform-ai-brain)
  BRAIN_NUDGE_MIN_TOOLS  tool calls before a session counts as long (default 20)
  BRAIN_NUDGE_DISABLE=1  turn it off
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

BRAIN = Path(os.environ.get("BRAIN_DIR") or Path.home() / "platform-ai-brain").expanduser().resolve()
STATE = Path(os.environ.get("CLAUDE_PLUGIN_DATA") or Path.home() / ".cache" / "platform-brain")
TOOL_USE = re.compile(r'"type":\s*"tool_use"')
ALREADY_SAVED = re.compile(r'\[brain-saved\]|"skill":\s*"brain:(learn|curate)"|/brain:(learn|curate)\b')
REASON = (
    "Before finishing: this was a long session and nothing was saved to the platform brain. If it produced "
    "something a teammate would otherwise rediscover (a root cause, a wrong assumption corrected, a "
    "version-specific quirk, a procedure that worked), tell the engineer in 2-3 lines what you would save "
    "and offer to save it with the brain:learn skill, which asks before pushing. If not, reply with one short "
    "line saying nothing needed saving. Don't repeat your previous answer."
)


def should_nudge(event: dict) -> bool:
    if os.environ.get("BRAIN_NUDGE_DISABLE") == "1" or event.get("stop_hook_active"):
        return False
    transcript = Path(event.get("transcript_path") or "")
    if not transcript.is_file():
        return False
    cwd = Path(event.get("cwd") or ".").resolve()
    if cwd == BRAIN or BRAIN in cwd.parents:
        return False  # working on the brain itself

    STATE.mkdir(parents=True, exist_ok=True)
    marker = STATE / f"nudged-{event.get('session_id', 'unknown')}"
    if marker.exists():
        return False
    for old in STATE.glob("nudged-*"):
        if time.time() - old.stat().st_mtime > 14 * 86400:
            old.unlink(missing_ok=True)

    text = transcript.read_text(encoding="utf-8", errors="ignore")
    try:
        minimum = int(os.environ.get("BRAIN_NUDGE_MIN_TOOLS", "20"))
    except ValueError:
        minimum = 20
    if len(TOOL_USE.findall(text)) < minimum or ALREADY_SAVED.search(text):
        return False
    marker.touch()
    return True


def main() -> None:
    try:
        event = json.load(sys.stdin)
        if should_nudge(event):
            print(json.dumps({"decision": "block", "reason": REASON}))
    except Exception:
        pass  # the hook must never trap Claude


if __name__ == "__main__":
    main()
