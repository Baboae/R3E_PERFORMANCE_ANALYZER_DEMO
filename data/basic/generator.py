from faker import Faker
from random import random
from random import choice
import string
from data.basic.model_classes import Player

def generate_id() -> str:
    chars = string.ascii_letters + string.digits
    return ''.join([choice(chars) for _ in range(6)])

def Create_Players(n: int) -> list[Player]:
    fake = Faker()
    new_id = generate_id()
    return [Player(
        "P-" + (str(i).zfill(6)),
        fake.name, generate_id(6), fake.country)]
if __name__ == "__main__":
    players = Create_Players(5)
    for p in players:
        print(p)
