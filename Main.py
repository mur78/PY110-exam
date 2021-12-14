import json
import random

from faker import Faker

import conf

Books_title = "books.txt"
Model_conf = "conf.py"
output_f = "output.txt"


def main():

    """Главная функция"""

    gen_1 = rand_book(1)
    list_ = [next(gen_1) for _ in range(100)]
    print(list_)

    with open(output_f, "w", encoding="utf-8") as f:
        json.dump(list_, f, ensure_ascii=False, indent=4)


def rand_title():
    """ Функция случайного заголовка"""

    with open(Books_title, 'r',encoding='utf8') as file:
        data = file.readlines()
        result = random.choice(data).strip()
        print(result)

    return result



def rand_year():
    """ Функция выбора случайного года"""

    result = random.randint(1800,2021)
    print(result)

    return result


def rand_pages():
    """ Функция выбора случайных страниц"""
    result = random.randint(1,100)

    return result


def rand_isbn13():
    """ Функция isbn13"""

    fake = Faker()
    Faker.seed(0)
    result = fake.isbn13()
    return result


def rand_rating():
    """ Функция рейтинга"""
    result = random.randint(1,5)
    return result

def rand_price():
    """ Функция цены"""
    result = random.randint(500, 2000)
    return result

def rand_book(pk: int = 1) -> dict:
    """ Функция генератора"""
    #cnt = 100
    model = conf.MODEL
    while True:
        book_1 = {
            "model": model,
            "pk": pk,
            "fields": {
                "title": rand_title(),
                "year": rand_year(),
                "pages": rand_pages(),
                "isbn13": rand_isbn13(),
                "rating": rand_rating(),
                "price" : rand_price(),
            }
        }
        yield book_1
        pk += 1


if __name__ == "__Main__":
    main()
