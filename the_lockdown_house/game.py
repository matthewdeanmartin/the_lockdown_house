"""
Main game loop
"""
import builtins
from typing import List, Optional, Dict, Any, Union

import the_lockdown_house.maps as maps
from the_lockdown_house.authenticate import login
from the_lockdown_house.commands import parse_command
from the_lockdown_house.maps import Mob, Player
from the_lockdown_house.payments import handle_payments, lookup_paid_users

LOG: List[str] = []



def print(*args, sep=' ', end='\n', file=None) -> None:
    if len(args) >= 1:
        LOG.append(args[0])
        builtins.print(args[0], sep=sep, end=end, file=file)
    else:
        builtins.print(sep=sep, end=end, file=file)


def open_crate(room: Dict[str, Any]) -> str:
    inventory = room["inventory"]

    inventory2 = []

    for item in inventory:
        # do something with item
        if isinstance(item, str):
            inventory2.append(item)
        if isinstance(item, list):
            inventory2.extend(item)

    room["inventory"] = inventory2
    return "some description"


def describe_things_in_room(inventory: List[Union[str, List[str]]]):
    # declare a variable, assign a initial value
    ght = []
    for item in inventory:
        # use that list, by adding thing to it
        # the thing is a list, say "crate"
        if isinstance(item, (str,)):
            ght.append(item)
        elif isinstance(item, (list,)):
            ght.append("crate")

    items_with_commas = ", ".join(ght)
    description = f"You can see {items_with_commas} laying around"
    print(description)
    return description


class Game():
    def __init__(self):
        self.map = maps.map_factory()

    def play(self, input) -> List[str]:
        # TODO: re-enable auth when we can save a game & ask for $$$$$
        password = input("give me your password.")
        username = input("give me your username.")
        d = login(username, password)
        if d:
            print(d)
            print("you are in!")
        else:
            print("GO AWAY HACKER!!!!!")
            exit()

        found = lookup_paid_users(username)
        money = 0
        if not found:
            money = input("i need more money")

        if found:
            print("Thanks for being a customer, you can play.")
        else:
            print("I don't see you on the paid customer list, you must pay now.")
            payment_was_successful, message = handle_payments(username, float(money))
            if payment_was_successful:
                print("the payment was successful")
                print(message)
            else:
                print("the payment was not successful")
                print(message)
                exit()




        LOG.clear()
        print("You are playing the Lockdown game. You are in an apartment full of rooms that you think you"
              "knew really, really well because you've been here since March 15, 2020, but are you sure there"
              "are not monsters and surprises here?\n\n")

        self.map.create_mobs()

        while True:
            description = self.print_current_description()
            user_text = input("Where do you want to go? ")
            result = parse_command(user_text)
            if not result:
                print("I don't understand. You must use two word commands starting with 'go', 'get', or 'use'")
                continue

            verb, predicate = result
            if verb == "quit":
                break
            if verb == "go":
                self.handle_motion_on_map(description, predicate)
                continue
            if verb == "get":
                self.handle_inventory_changes(description, predicate)
                continue
            if verb == "use":
                foo = self.map.player.use(predicate)
                print(foo)
                continue
            if verb == "inventory":
                print(", ".join(self.map.player.inventory))
                continue
            if verb == "hp":
                print(f"You have {self.map.player.health_points} left")
                continue
            if verb == "fight":
                self.describe_fight(predicate)
                continue
            if verb == "open":
                open_crate(room=self.map.rooms[self.map.player.current_location])

            print(f"Sorry, don't know how to handle the command {verb} {predicate}")

        print("Ok, bye!")
        return LOG

    def handle_motion_on_map(self, current_room: Dict[str, Dict[str, str]], direction: str) -> List[str]:
        """Update player's current location if possible, else warn that it is not possible"""
        messages = []
        message = "Okay, lets see if that is possible"
        messages.append(message)
        if direction in current_room["links"]:
            message = f"You are going {direction}"
            messages.append(message)
            self.map.player.current_location = current_room["links"][direction]
        else:
            message = "You can't go that way!"
            messages.append(message)
        for current in messages:
            print(current)
        return messages

    def handle_inventory_changes(self, current_room: Dict[str, Any], predicate: str) -> None:
        if predicate in current_room["inventory"]:
            self.map.player.inventory.append(predicate)
            current_room["inventory"].remove(predicate)
            print(f"Picked up {predicate}")
        else:
            print(f"I don't see any {predicate} here, do you?")

    def describe_fight(self, predicate):
        target_mob = self.find_mob_in_room(predicate)
        if target_mob:
            description = self.fight(self.map.player, target_mob)
            print(description)
        else:
            print(f"You idiot! You can't fight {predicate}, they are not in the room!")

    def print_current_description(self):
        print(f"You are in the {self.map.player.current_location}")
        current_room = self.map.rooms[self.map.player.current_location]
        self.pretty_print_directions(current_room["links"])
        describe_things_in_room(current_room["inventory"])
        for mob in current_room["mobs"]:
            print(f"You can see a {mob.name} in this room")
        print()
        return current_room

    def pretty_print_directions(self, links: Dict[str, str]) -> str:
        zum = []
        for direction, _ in links.items():
            zum.append(direction)

        comma = ", "
        zum.sort()
        directions = comma.join(zum)

        print(f"You can go {directions}")
        return directions

    def find_mob_in_room(self, predicate: str) -> Optional[Mob]:
        target_mob = None
        mobs: List[Mob] = self.map.rooms[self.map.player.current_location]["mobs"]
        for possible_mob in mobs:
            if predicate.lower() == possible_mob.name.lower():
                target_mob = possible_mob
        return target_mob

    def fight(self, player: "Player", mob: "Mob") -> str:
        description = "They fought... it was tense. "
        player_has_sword = "sword" in player.inventory
        mob_has_sword = "sword" in mob.inventory
        description, mob_damage = self.calculate_damage_to_mob(description, player_has_sword)
        mob.health_points = mob.health_points - mob_damage

        description += f"You caused {mob_damage} points of damage. "

        player_damage = self.calculate_damage_to_player(mob_has_sword)
        player.health_points = player.health_points - player_damage

        description += f"You lost {player_damage} hp"

        # if
        # you lose {predicate} hp
        return description

    def calculate_damage_to_player(self, mob_has_sword: bool) -> int:
        if mob_has_sword:
            player_damage = 50
        else:
            player_damage = 30
        return player_damage

    def calculate_damage_to_mob(self, description, player_has_sword):
        if player_has_sword:
            mob_damage = 50
            description += f"Good thing you have a sword. "
        else:
            mob_damage = 1
        return description, mob_damage


if __name__ == '__main__':
    def run():
        game = Game()
        game.play(input)


    run()
