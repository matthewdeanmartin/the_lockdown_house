# x = {}
# x["key"] ="value"

def test_create_dictionary_of_numbers():
    numbers = {}
    numbers["one"] = 1
    numbers["two"] = 2
    numbers["three"] = 3

    assert numbers == {
        "one": 1,
        "two": 2,
        "three": 3
    }


# x = []
# x.append(1)

def test_create_list_of_numbers():
    numbers = []
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    assert numbers == [1, 2, 3]


# x = set()
# x.add(1)

def test_create_set_of_numbers():
    numbers = method_name()
    assert numbers == {1, 2, 3}


def method_name():
    numbers = set()
    numbers.add(1)
    numbers.add(2)
    numbers.add(3)
    return numbers
