"""

2 word commands

GET {ITEM}

GO {DIRECTION}

USE {ITEM}
"""
from typing import Tuple, Optional


def parse_command(command_text: str) -> Optional[Tuple[str, str]]:
    command_text = command_text.lower().strip()
    while "  " in command_text:
        command_text = command_text.replace("  ", " ")
    parts = command_text.split(" ")
    if len(parts) < 2:
        print("Bad command!")
        return None
    verb = parts[0]
    predicate = parts[1]
    if verb == "go":
        if len(predicate) >= 1:
            predicate = predicate[0]
        else:
            print("Missing direction!")
            return None
    return verb, predicate
