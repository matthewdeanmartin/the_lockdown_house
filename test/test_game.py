from the_lockdown_house.game import Game


class Input():
    commands = []
    count = 0

    def __init__(self, commands):
        self.commands = commands

    def __call__(self, *args, **kwargs):
        result = self.commands[self.count]
        self.count += 1
        return result


def test_play():
    game = Game()
    result = game.play(Input(["go north",
                              "go south",
                              "",
                              "quit"]))
    assert result


def test_play_quit():
    game = Game()
    result = game.play(Input(["quit"]))
    assert len(result) < 20


def test_handle_motion_on_map():
    direction = "s"
    game_map = {
        "links": {
            "n": "kids bed room",
            "s": "NaN"
        }
    }
    game = Game()
    game.map.player.current_location = "HOME"
    assert game.map.player.current_location == 'HOME'
    fre = game.handle_motion_on_map(game_map, direction)
    assert game.map.player.current_location == 'NaN'


def test_handle_motion_on_map_cant_do_that():
    desired_direction = "w"
    game_map = {
        "links": {
            "n": "kids bed room",
            "s": "NaN"
        }
    }
    game = Game()
    game.map.player.current_location = "HOME"
    assert game.map.player.current_location == 'HOME'
    messages = game.handle_motion_on_map(game_map, desired_direction)
    found_cant = False
    for message in messages:
        if "can't" in message:
            found_cant = True
    assert found_cant
    assert game.map.player.current_location == 'HOME'


def test_play_long_game():
    game = Game()
    result = game.play(Input([
        "go north",
        "go south",
        "use sword",
        "use crate",
        "inventory",
        "OP crate",
        "go w",
        "go e",
        "get food",
        "quit"]))
    assert result


def test_pretty_print_directions():
    # arrange
    g = Game()
    test_links = {
        "n": "kitchen",
        "e": "hall way n",
    }
    # act
    d = g.pretty_print_directions(links=test_links)
    # assert
    assert d == "n, e"
