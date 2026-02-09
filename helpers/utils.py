import random
import string


def random_email():
    letters = string.ascii_lowercase
    prefix = ''

    for _ in range(10):
        prefix += random.choice(letters)

    return prefix + '@test.ru'
