from the_lockdown_house.commands import parse_command, validate_parse_directions, parse_short_cuts


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
    assert validate_parse_directions("go", "nowhere") == ("go", "n")  # hmm??
    assert validate_parse_directions("go", "noooooooooooooooooooooooooooooorth") == ("go", "n")


def test_validate_parse_bad_directions():
    return_value = validate_parse_directions("go", "")
    assert return_value[0] is None
    assert return_value[1]


def test_validate_parse_bad_directions_not_nsew():
    zoobydooby = validate_parse_directions("go", "zoobydooby")
    assert zoobydooby[0] is None
    assert zoobydooby[1]


def test_parse_short_cuts():
    # arrange - set up a known initial state, arguments, etc.
    users_command = "go n"
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == users_command


def test_parse_short_cuts_wild_text():
    # arrange - set up a known initial state, arguments, etc.
    users_command = "lksdjfg;lkwejg;lkjsdefg;lkjsdefg"
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == users_command


def test_parse_short_cuts_empty_string():
    # arrange - set up a known initial state, arguments, etc.
    users_command = ""
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == users_command


def test_parse_short_cuts_n_becomes_go_north():
    # arrange - set up a known initial state, arguments, etc.
    users_command = "n"
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == "go north"


def test_parse_short_cuts_s_becomes_go_south():
    # arrange - set up a known initial state, arguments, etc.
    users_command = "s"
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == "go south"


def test_parse_short_cuts_e_becomes_go_east():
    # arrange - set up a known initial state, arguments, etc.
    users_command = "e"
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == "go east"


def test_parse_short_cuts_W_becomes_go_west_capitalized():
    # arrange - set up a known initial state, arguments, etc.
    users_command = "W"
    # act- call a function with known arguments
    kll = parse_short_cuts(command_text=users_command)

    # assert - assert that we get the result (return value) that we expected
    assert kll == "go west"
