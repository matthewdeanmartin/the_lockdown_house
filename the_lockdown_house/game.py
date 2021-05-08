"""
Main game loop
"""
from text_adventure.commands import parse_command
from text_adventure.maps import MAP, MOBS, create_mobs, create_player, PLAYER


def play():
    print("You are playing the @*% game.")
    create_mobs()

    create_player()

    # place mobs on map
    for mob in MOBS:
        MAP[mob.current_location]["mobs"].append(mob)

    while True:
        print(f"You are in the {PLAYER.current_location}")
        description = MAP[PLAYER.current_location]
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
            print(PLAYER.inventory)
            continue

        result = parse_command(user_text)
        if not result:
            print("I don't understand. You must use two word commands starting with 'go', 'get', or 'use'")
            continue

        verb, predicate = result
        if verb == "go":
            if predicate in description["links"]:
                print(f"You are going {predicate}")
                PLAYER.current_location = description["links"][predicate]
            else:
                print("You can't go that way!")
        if verb == "get":
            if predicate in description["inventory"]:
                PLAYER.inventory.append(predicate)
                description["inventory"].remove(predicate)
            else:
                print(f"I don't see any {predicate} here, do you?")
        if verb == "use":
            print("Don't know how yet!")


play()
