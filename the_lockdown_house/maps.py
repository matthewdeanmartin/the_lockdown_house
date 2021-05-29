"""
Data structures with

Place (can be in a building or outside)
Connected by n,s,e,w

Can have items at a place

Can have mob  at place

    S
  E   W
    N
"""
import dataclasses
from typing import Optional


# PLAYER: Optional["Player"] = None
#
# MOBS: List["Mob"] = []


@dataclasses.dataclass
class Player():
    current_location = "living room"
    inventory = []
    name = "Tano"
    health_points = 253

    def use(self, predicate: str) -> str:
        if predicate not in self.inventory:
            message = "You can't use that yet."
            return message
        message = ""

        if predicate == "food":
            message += f"You ate the food it tasted like {predicate}. "
            self.health_points += 100
            if self.health_points > 253:
                # You can only have 253 points
                self.health_points = 253
        else:
            message += f"I don't know how to use {predicate}, yet. "

        if predicate in ["food", "crate", "potion", "OP_crate", ]:
            message += f"You no longer have {predicate} in inventory. "
            self.inventory.remove(predicate)

        return message

    def fight(self, mob: "Mob", with_item: str) -> int:
        if with_item == "sword":
            damage = 50
        elif with_item == "toy sword":
            damage = 10
        else:
            print(f"You can't fight with {with_item}")
            damage = 0
        print(f"You did {damage} damage to {mob.name}.")
        mob.health_points -= damage
        return damage


@dataclasses.dataclass
class Mob():
    current_location = ""
    inventory = []
    name = ""
    health_points = 50

    def give(self, item: str) -> Optional[str]:
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None


@dataclasses.dataclass
class Map():

    def __init__(self):
        self.rooms = {}
        self.player = Player()
        self.mobs = []

    def create_mobs(self):
        tasi = Mob()
        tasi.inventory.extend(["cookies", "donuts", "lion toy"])
        tasi.name = "Tasi"
        tasi.current_location = "kids bedroom"
        self.mobs.append(tasi)

        mom = Mob()
        mom.inventory.extend(["bagel", "pick axe", "car keys"])
        mom.current_location = "master bedroom"
        mom.name = "Mom"
        self.mobs.append(mom)

        dad = Mob()
        dad.current_location = "living room"
        dad.inventory.extend(["sword", "spell book"])
        dad.name = "Dad"
        self.mobs.append(dad)

        # place mobs on map
        for mob in self.mobs:
            self.rooms[mob.current_location]["mobs"].append(mob)

    def validate_links(self):
        complaints = []
        for room, description in self.rooms.items():
            for direction, linked_room in description["links"].items():
                if linked_room in self.rooms.keys():
                    pass
                else:
                    complaints.append(f"Room {room} has a bad link '{linked_room}' is not a known place")
        for room, description in self.rooms.items():
            if not description["links"]:
                complaints.append(f"Print can't exit room {room}")

        all_links = []
        for other_room, description in self.rooms.items():
            links = description["links"].items()
            for link, reachable_room in links:
                all_links.append(reachable_room)

        for room in self.rooms.keys():
            if room in all_links:
                continue
            else:
                complaints.append(f"Room {room} is not reachable!")
        return complaints

    def master_inventory(self):
        all_items = []
        for room, description in self.rooms.items():
            all_items.extend(description["inventory"])
        for mob in self.mobs:
            all_items.extend(mob.inventory)
        all_items.extend(self.player.inventory)
        return all_items


def map_factory() -> Map:
    map = Map()
    map.rooms = {
        "master bedroom": {
            "links": {
                "e": "hallway south"
            },
            "inventory": ["sword", "cookies", "milk"],
            "mobs": []
        },
        "kids bedroom": {
            "links": {
                "e": "hallway north"
            },
            "inventory": ["toy sword", "money"],
            "mobs": []
        },
        "far bedroom": {
            "links": {
                "s": "hallway north"
            },
            "inventory": [],
            "mobs": []
        },
        "hallway south": {
            "links": {
                "w": "master bedroom",
                "n": "hallway north",
                "e": "living room",
                "s": "bathroom"
            },
            "inventory": [],
            "mobs": []
        },
        "hallway north": {
            "links": {
                "w": "kids bedroom",
                "s": "hallway south",
                "n": "far bedroom",
                "e": "chamber"
            },
            "inventory": [],
            "mobs": []
        },
        "living room": {
            "links": {
                "s": "kitchen",
                "w": "hallway south"
            },
            "inventory": [["apple", "orange"]],
            "mobs": []
        },
        "bathroom": {
            "links": {
                "s": "kitchen",
                "w": "hallway south"
            },
            "inventory": [],
            "mobs": []
        },
        "kitchen": {
            "links": {
                "s": "kitchen",
                "w": "hallway south",
                "n": "sus room"

            },
            "inventory": ["food", ["dark sword", "cat_food"]],
            "mobs": []
        },
        "chamber": {
            "links": {
                "w": "hallway north"
            },
            "inventory": ["food", "HOLY_sword", "godly_power_ball", ],
            "mobs": []
        },
        "secret base": {
            "description": "it is very secret",
            "links": {
                "e": "sus room",
                "w": "infinity room"
            }, "mobs": [], },
        "sus room": {
            "description": "when the imposter is sus....",
            "links": {
                "n": "basement",
                # "s": "among us",
                "e": "infinity room"
            },
            "inventory": ["food"],
            "mobs": []
        },
        "infinity room": {
            "description": "when the imposter is sus....",
            "links": {
                "e": "infinity room",
                "w": "NaN"
            },
            "inventory": [],
            "mobs": []
        },
        "basement": {
            "description": "you see big white squares and only blue sky and no moon or sun",
            "links": {
                "e": "infinity room",
                "w": "NaN"
            }, "inventory": ["food"],
            "mobs": []
        },
        "NaN": {
            "description": "",
            "links": {
            }, "inventory": ["food"],
            "mobs": []
        },
        "room of the gods": {
            "description": "WHAt THE H---!!!!",
            "links": {
                "e": "infinity room",
                "w": "NaN",
            },
            "mobs": ["the GOD"]
        }
    }
    tiky = {
        "description": "WHAt THE H---!!!!",
        "links": {
            "w": "sus room",
            "s": "NaN",
        },
        "mobs": ["the GOD"]
    }
    map.rooms["tiky"] = tiky
    # x = {}
    # x["key"] ="value"

    return map


if __name__ == '__main__':
    # complaints = validate_links()
    # for complaint in complaints:
    #     print(complaint)
    def run():
        game_map = Map()
        print(set(game_map.master_inventory()))


    run()
