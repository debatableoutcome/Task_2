import random
import string


def random_email():
    number = random.randint(10000, 99999)
    return f'test_{number}@test.ru'
