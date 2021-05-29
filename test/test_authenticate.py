from the_lockdown_house.authenticate import login


def test_login():
    assert login("mmartin", "chunkstyle") == True


def test_spider_can_login():
    ff = login("spider", "fdy")
    assert ff == True
