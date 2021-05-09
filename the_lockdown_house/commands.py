"""

2 word commands

GET {ITEM}

GO {DIRECTION}

USE {ITEM}

1 word
INVENTORY
"""
from typing import Tuple, Optional


def parse_command(command_text: str) -> Optional[Tuple[str, str]]:
    """Split command into two words"""

    # clean up input, remove junk and extra spaces
    command_text = command_text.lower().strip()
    while "  " in command_text:
        command_text = command_text.replace("  ", " ")

    # split on spaces
    parts = command_text.split(" ")

    # handle one word commands
    if len(parts) == 1:
        verb = parts[0]
        predicate = ""
        if verb in ["inventory"]:
            return verb, predicate

    # handle bad input (too short)
    if len(parts) < 2:
        print("Bad command!")
        return None

    # Parse into verb and predicate
    verb = parts[0]
    predicate = parts[1]

    # simplify and validate direction
    if verb == "go":
        return validate_parse_directions(verb, predicate)

    return verb, predicate


def validate_parse_directions(verb: str, direction: str) -> Tuple[Optional[str], Optional[str]]:
    """Parse north, south, east, west to n, s, e, w and if the user types trash
    insult them and return a tuple like, (None, some validation message)"""
    if len(direction) >= 1:
        # shorten [N]orth to N
        direction = direction[0]
        if direction in "nsew":
            return verb, direction

        else:
            return None,"Bad direction, you idiot! Only n, s, e, w!"

    else:
        return None, "Missing direction"


print(validate_parse_directions("go", "zud"))