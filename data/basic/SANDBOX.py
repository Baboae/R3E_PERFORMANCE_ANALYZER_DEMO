from faker import Faker
from random import random
from random import choice
import string
fake = Faker()

def generate_id() -> str:
    chars = string.ascii_letters + string.digits
    return ''.join([choice(chars) for _ in range(6)])

print(generate_id())
