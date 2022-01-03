import random
from faker import Faker


def rand_author() -> list:
    """ Функция выбора случайного автора"""

    n = random.randint(1, 3)
    #result = []
    fake = Faker()
    # for _ in range(n):
    #     result.append(fake.name())
    result = [fake.name() for _ in range(n)]
    print(result)
    return result

rand_author()
