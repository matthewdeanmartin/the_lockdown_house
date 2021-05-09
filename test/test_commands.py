from the_lockdown_house.commands import parse_command, validate_parse_directions


def test_parse_command():
    assert parse_command("go north") == ("go", "n")
    assert parse_command("get sword") == ("get", "sword")
    assert parse_command("get food") == ("get", "food")
    assert parse_command("use food") == ("use", "food")
    assert parse_command(" Use    foOd now!!!!") == ("use", "food")
    assert parse_command("inventory") == ("inventory", "")
    assert parse_command("erth5yuirhtjguiejui4envbgme654iuyhjyre5imnvutiowjgfo,") is None
    assert parse_command("go") is None


def test_parse_fight_command():
    assert parse_command("fight dad") == ("fight", "dad")


def test_validate_parse_directions():
    assert validate_parse_directions("go", "s") == ("go", "s")
    assert validate_parse_directions("go", "south") == ("go", "s")
    assert validate_parse_directions("go", "nowhere") == ("go", "n") # hmm??
    assert validate_parse_directions("go", "noooooooooooooooooooooooooooooorth") == ("go", "n")


def test_validate_parse_bad_directions():
    return_value = validate_parse_directions("go", "")
    assert return_value[0] is None
    assert return_value[1]

def test_validate_parse_bad_directions_not_nsew():
    zoobydooby = validate_parse_directions("go", "zoobydooby")
    assert zoobydooby[0] is None
    assert zoobydooby[1]