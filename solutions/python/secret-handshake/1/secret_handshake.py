from __future__ import annotations

ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> list[str]:
    commands = [action for action, digit in zip(ACTIONS, binary_str[-1:-5:-1]) if digit == "1"]

    if binary_str[0] == "1":
        commands.reverse()

    return commands
