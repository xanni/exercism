from __future__ import annotations

ACTIONS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str) -> list[str]:
    commands = [ACTIONS[i] for i in range(4) if binary_str[4 - i] == "1"]

    if binary_str[0] == "1":
        commands.reverse()

    return commands
