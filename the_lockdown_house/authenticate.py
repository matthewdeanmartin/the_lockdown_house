"""
Authenticate user so we can collect money
"""

# List
from typing import Dict

user_mmartin: Dict[str, str] = {
    "name": "mmartin",
    "password": "chunkstyle"
}

foobar = {"name": "tano",
          "password": "fdy"
          }

user_eloise = {
    "name": "eloise",
    "password": "some_secret"
}
user_spider = {
    "name": "spider",
    "password": "creps"
}

user_database = [
    user_eloise,
    user_mmartin,
    foobar,
    user_spider,
]


def login(player_username: str, player_password: str) -> bool:
    for current_user in user_database:
        # print(user["name"])
        if player_password == current_user["password"] and current_user["name"] == player_username:
            return True
    return False


if __name__ == '__main__':
    def run():
        username = input("what is your username")
        password = input("what is your password")
        if login(username, password):
            print("you are in!")
        else:
            print("go away hacker")
            exit()


    run()
