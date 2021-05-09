from the_lockdown_house.maps import validate_links


def test_validate_map():
    assert len(validate_links()) == 0
