from the_lockdown_house.maps import Player


def test_player_basics():
    some_player = Player()
    assert some_player
    assert some_player.name


def test_player_use_food_reduces_inventory():
    some_player = Player()
    some_player.inventory.append("food")
    some_player.use("food")
    assert "food" not in some_player.inventory


def test_player_use_food_on_empty_inventory_complains():
    some_player = Player()
    # some_player.inventory.append("food")
    assert not some_player.inventory
    message = some_player.use("food")
    assert "can't" in message
    assert "food" not in some_player.inventory


def test_player_use_food_will_increase_health():
    some_player = Player()
    some_player.inventory.append("food")

    starting_points = some_player.health_points
    # check starting conditions
    assert some_player.health_points > 0
    assert "food" in some_player.inventory

    message = some_player.use("food")

    # check final conditions
    assert message
    assert some_player.health_points > 0
    assert some_player.health_points > starting_points or some_player.health_points == 253
    assert some_player.health_points <= 253
    assert "food" not in some_player.inventory
