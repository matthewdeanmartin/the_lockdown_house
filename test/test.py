from text_adventure.commands import parse_command
from text_adventure.maps import validate_links


def test_parse_command():
    assert parse_command("go north") == ("go", "n")
    assert parse_command("get sword") == ("get", "sword")
    assert parse_command("get food") == ("get", "food")
    assert parse_command("use food") == ("use", "food")
    assert parse_command(" Use    foOd now!!!!") == ("use", "food")

def test_validate_map():
    assert len(validate_links())==0