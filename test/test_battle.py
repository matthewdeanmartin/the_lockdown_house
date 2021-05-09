from the_lockdown_house.game import fight, calculate_damage_to_mob, calculate_damage_to_player
from the_lockdown_house.maps import Player, Mob


def test_fight():
    test_player = Player()
    test_mob = Mob()
    description = fight(test_player, test_mob)
    assert description

def test_calculate_damage_to_mob():
    initial_description = "Starting.."
    description, mob_damage_with = calculate_damage_to_mob(initial_description,player_has_sword= True)
    description, mob_damage_with_out = calculate_damage_to_mob(initial_description, player_has_sword=False)
    assert mob_damage_with > mob_damage_with_out

def test_calculate_damage_to_player():
    initial_description = "Starting.."
    player_damage_with = calculate_damage_to_player(mob_has_sword= True)
    player_damage_with_out = calculate_damage_to_player(mob_has_sword= False)
    assert player_damage_with > player_damage_with_out
