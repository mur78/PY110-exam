import json
import random

from faker import Faker

import conf

BOOKS_TITLE = "books.txt"
MODEL_CONF = "conf.py"
OUTPUT_F = "output.txt"


def main():
    """Главная функция"""

    gen_1 = rand_book(1)
    list_ = [next(gen_1) for _ in range(100)]
    print(list_)
    with open(OUTPUT_F, "w", encoding="utf-8") as f:
        json.dump(list_, f, ensure_ascii=False, indent=4)


def rand_title() -> str:
    """ Функция выбора случайного заголовка"""

    with open(BOOKS_TITLE, 'r', encoding='utf8') as file:
        data = file.readlines()
        result = random.choice(data).strip()
        print(result)
    return result


def rand_year() -> int:
    """ Функция выбора случайного года"""

    result = random.randint(1800, 2021)
    print(result)
    return result


def rand_pages() -> int:
    """ Функция выбора случайных страниц"""

    result = random.randint(1, 100)
    return result


def rand_isbn13() -> str:
    """ Функция isbn13"""

    fake = Faker()
    Faker.seed(0)
    result = fake.isbn13()
    return result


def rand_rating() -> int:
    """ Функция случайного рейтинга"""

    result = random.randint(1, 5)
    return result


def rand_price() -> int:
    """ Функция формирования цены"""

    result = random.randint(500, 2000)
    return result


def rand_author() -> list:
    """ Функция выбора случайного автора"""

    n = random.randint(1, 3)
    fake = Faker()
    return [fake.name() for _ in range(n)]


def rand_book(pk: int = 1) -> dict:
    """ Функция генератора книг"""

    model = conf.MODEL
    while True:
        book_1 = {
            "model": model,
            "pk": pk,
            "fields":
                {
                    "title": rand_title(),
                    "year": rand_year(),
                    "pages": rand_pages(),
                    "isbn13": rand_isbn13(),
                    "rating": rand_rating(),
                    "price": rand_price(),
                    "author": rand_author()
                }
            }
        yield book_1
        pk += 1


if __name__ == "__Main__":
    main()
