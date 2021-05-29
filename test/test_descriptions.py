from the_lockdown_house.game import describe_things_in_room, open_crate


def test_describe_things_in_room():
    # arrange
    inventory = ["food", ["dark sword", "cat_food"]]
    # act
    d = describe_things_in_room(inventory)

    # assert
    # You can see food, crate laying around
    assert d == "You can see food, crate laying around"

def test_open_crate():
    # arrange
    inventory = [
        "food",  # first item
        ["dark sword", "cat_food"],  # second item
    ]
    assert len(inventory) == 2
    room = {
        "description": "when the imposter is sus....",
        "links": {
            "e": "infinity room",
            "w": "NaN"
        },
        "inventory": inventory,
        "mobs": []
    }
    # act
    jke = open_crate(room)


    # assert
    assert len(room["inventory"]) == 3


def add(a, b):
    return a + b


result = add

print(result)
