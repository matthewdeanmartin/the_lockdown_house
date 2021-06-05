"""

2 word commands


GO {DIRECTION}

USE {ITEM}

1 word
INVENTORY
"""
from typing import Optional, Tuple


def parse_chinese(command_text: str) -> str:
    raise NotImplementedError("Maybe we should implement this someday")


def parse_short_cuts(command_text: str) -> str:
    # TODO: replace command text with long form if shortcut found
    command_text = command_text.lower()

    if command_text == "n":
        command_text = "go north"
        return command_text

    if command_text == "w":
        command_text = "go west"

    if command_text == "e":
        command_text = "go east"
    if command_text == "s":
        command_text = "go south"
    # ELSE: return users text unchanged DONE!
    return command_text


def parse_command(command_text: str) -> Optional[Tuple[str, str]]:
    """Split command into two words"""

    # clean up input, remove junk and extra spaces
    command_text = command_text.lower().strip()
    while "  " in command_text:
        command_text = command_text.replace("  ", " ")

    command_text = parse_short_cuts(command_text)

    # split on spaces
    parts = command_text.split(" ")

    # handle one word commands
    if len(parts) == 1:
        verb = parts[0]
        predicate = ""
        if verb in ["inventory", "hp", "quit"]:
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
        part1, part2 = validate_parse_directions(verb, predicate)
        # handle validation
        if not part1:
            print(part2)
        return part1, part2

    if verb == "open":
        if predicate == "crate":
            return verb, predicate
        else:
            return None, "You can only open crates"

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
            return None, "Bad direction, you idiot! Only n, s, e, w!"

    else:
        return None, "Missing direction"


if __name__ == '__main__':
    print(validate_parse_directions("go", "zud"))

crate = []
crate.append("potion")
crate.append("dark sword")
