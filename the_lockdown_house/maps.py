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
from typing import Optional, List, Dict

PLAYER:Optional["Player"]= None

MOBS:List["Mob"] = []

MAP = {
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
        "inventory": [],
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
        "inventory": ["food"],
        "mobs": []
    },
    "chamber": {
        "links": {
            "w": "hallway north"
        },
        "inventory": ["food"],
        "mobs": []
    },

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
        },"inventory": ["food"],
        "mobs": []
    },
    "NaN": {
        "description": "",
        "links": {
        },"inventory": ["food"],
        "mobs": []
    },
}

@dataclasses.dataclass
class Player():
    current_location = "living room"
    inventory = []
    name = "Tano"
    health_points = 277

    def fight(self, mob:"Mob", with_item:str)->int:
        if with_item == "sword":
            damage =  50
        elif with_item == "toy sword":
            damage = 10
        else:
            print(f"You can't fight with {with_item}")
            damage =0
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

def create_mobs():
    tasi = Mob()
    tasi.inventory.extend(["cookies", "donuts", "lion toy"])
    tasi.name = "Tasi"
    tasi.current_location = "kids bedroom"
    MOBS.append(tasi)

    mom = Mob()
    mom.inventory.extend(["bagel", "pick axe", "car keys"])
    mom.current_location = "master bedroom"
    mom.name = "Mom"
    MOBS.append(mom)

    dad = Mob()
    dad.current_location = "living room"
    dad.inventory.extend(["sword", "spell book"])
    dad.name = "Dad"
    MOBS.append(dad)

def create_player()->None:
    global PLAYER
    PLAYER = Player()

def validate_links():
    complaints = []
    for room, description in MAP.items():
        for direction, linked_room in description["links"].items():
            if linked_room in MAP.keys():
                pass
            else:
                complaints.append(f"Room {room} has a bad link '{linked_room}' is not a known place")
    for room, description in MAP.items():
        if not description["links"]:
            complaints.append(f"Print can't exit room {room}")

    all_links = []
    for other_room, description in MAP.items():
        links = description["links"].items()
        for link, reachable_room in links:
            all_links.append(reachable_room)

    for room in MAP.keys():
        if room in all_links:
            continue
        else:
            complaints.append(f"Room {room} is not reachable!")
    return complaints


def master_inventory():
    all_items = []
    for room, description in MAP.items():
        all_items.extend(description["inventory"])
    for mob in MOBS:
        all_items.extend(mob.inventory)
    all_items.extend(PLAYER.inventory)
    return all_items

if __name__ == '__main__':
    # complaints = validate_links()
    # for complaint in complaints:
    #     print(complaint)
    create_mobs()
    create_player()
    print(set(master_inventory()))