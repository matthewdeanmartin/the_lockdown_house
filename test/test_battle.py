from the_lockdown_house.game import Game
from the_lockdown_house.maps import Player, Mob


def test_fight():
    test_player = Player()
    test_mob = Mob()
    test_game = Game()
    description = test_game.fight(test_player, test_mob)
    assert description

def test_calculate_damage_to_mob():
    initial_description = "Starting.."
    test_game = Game()
    description, mob_damage_with = test_game.calculate_damage_to_mob(initial_description,player_has_sword= True)
    description, mob_damage_with_out = test_game.calculate_damage_to_mob(initial_description, player_has_sword=False)
    assert mob_damage_with > mob_damage_with_out

def test_calculate_damage_to_player():
    test_game = Game()
    player_damage_with = test_game.calculate_damage_to_player(mob_has_sword= True)
    player_damage_with_out = test_game.calculate_damage_to_player(mob_has_sword= False)
    assert player_damage_with > player_damage_with_out
