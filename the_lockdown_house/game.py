"""
Main game loop
"""
import the_lockdown_house.maps as map
from the_lockdown_house.commands import parse_command


def play():
    print("You are playing the @*% game.")
    map.create_mobs()

    map.create_player()

    # place mobs on map
    for mob in map.MOBS:
        map.MAP[mob.current_location]["mobs"].append(mob)

    while True:
        print(f"You are in the {map.PLAYER.current_location}")
        description = map.MAP[map.PLAYER.current_location]
        for direction, next_room in description["links"].items():
            print(f"You can go {direction}")
        for item in description["inventory"]:
            print(f"You can see a {item} laying around")
        for mob in description["mobs"]:
            print(f"You can see a {mob.name} in this room")
        print()

        user_text = input("Where do you want to go? ")
        if user_text == "quit":
            break
        if user_text == "inventory":
            print(map.PLAYER.inventory)
            continue

        result = parse_command(user_text)
        if not result:
            print("I don't understand. You must use two word commands starting with 'go', 'get', or 'use'")
            continue

        verb, predicate = result
        if verb == "go":
            if predicate in description["links"]:
                print(f"You are going {predicate}")
                map.PLAYER.current_location = description["links"][predicate]
            else:
                print("You can't go that way!")

        if verb == "get":
            if predicate in description["inventory"]:
                map.PLAYER.inventory.append(predicate)
                description["inventory"].remove(predicate)
                print(f"Picked up {predicate}")
            else:
                print(f"I don't see any {predicate} here, do you?")

        if verb == "use":
            print("Don't know how yet!")

        if verb == "inventory":
            print(", ".join(map.PLAYER.inventory))


def fight(player: map.Player, mob: map.Mob):
    description = "They fought... it was tense. "
    player_has_sword = "sword" in player.inventory
    mob_has_sword = "sword" in mob.inventory
    description, mob_damage =calculate_damage_to_mob(description, player_has_sword)
    mob.health_points = mob.health_points - mob_damage

    description += f"You caused {mob_damage} points of damage. "

    player_damage = calculate_damage_to_player(mob_has_sword)
    player.health_points = player.health_points - player_damage

    description += f"You lost {player_damage} hp"

    return description


def calculate_damage_to_player(mob_has_sword:bool)->int:
    if mob_has_sword:
        player_damage = 50
    else:
        player_damage = 30
    return player_damage


def calculate_damage_to_mob(description, player_has_sword):
    if player_has_sword:
        mob_damage = 50
        description += f"Good thing you have a sword. "
    else:
        mob_damage = 1
    return description, mob_damage


if __name__ == '__main__':
    play()
