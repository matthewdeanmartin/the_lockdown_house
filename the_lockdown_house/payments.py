"""
Handle money
"""
import csv

# print(2 in [6,7,8,9, 2])
from typing import Tuple


def lookup_paid_users(username: str) -> bool:
    with open("payments.csv", "r", newline="") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if username in row:
                return True

        return False


def create_paid_user(username: str, paid: float):
    with open('payments.csv', 'a', newline="") as csv_file:
        writer = csv.writer(csv_file)
        row = [username, paid]
        writer.writerow(row)


def handle_payments(username: str, money: float) -> Tuple[bool, str]:
    found_user = lookup_paid_users(username)
    if found_user:
        return True, "thank you for your money!"

    if money < 20:
        return False, "you did't pay, pay more!"

    create_paid_user(username, money)
    return True, "thank you for your money!"


def how_much_money_did_we_make():
    pass


if __name__ == '__main__':
    # create_paid_user(username="tano", paid=20)
    # print(lookup_paid_users(username="pia"))
    handle_payments("akjsdhjfklasdf", 20)

    # z="jack"
    # b=18
    # handle_payments(z,b)
