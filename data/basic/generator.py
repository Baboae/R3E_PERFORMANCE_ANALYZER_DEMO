from faker import Faker
from random import random
from random import choice
import string
from data.basic.model_classes import Player

def generate_id() -> str:
    chars = string.ascii_letters + string.digits
    return ''.join([choice(chars) for _ in range(6)])
def generate_players(n: int) -> list[Player]:
    fake = Faker()
    for i in range(n):
        return [Player(
            "P-" + generate_id(),
            fake.name(),
            fake.country())]
if __name__ == "__main__":
    i = 1
    for i in range(4):
        print(generate_players(i))