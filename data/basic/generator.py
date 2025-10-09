from faker import Faker
from random import random
from random import choice
import string
from data.basic.model_classes import Player
#region id generator
def generate_id() -> str:
    chars = string.ascii_letters + string.digits
    return ''.join([choice(chars) for _ in range(6)])
#endregion
#region player generator
def generate_Players(howmuch: int = 1, locale: str = "en_US") -> list[Player]:
    fake = Faker(locale)
    ret_Players = []
    for i in range(howmuch):
        ret_Players.append(Player(generate_id(), fake.name(), fake.country()))
    return ret_Players
#endregion
#region test
if __name__ == '__main__':
    n = 100
    mylist = generate_Players(n)
    with open("player_list.txt", "w") as players_file:
        n = 100
        mylist = generate_Players(n)
        for i in range(n):
            print(mylist[i])
            players_file.write("{0}\n".format(str(mylist[i])))
#endregion