import requests


def hello(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


def multiply(a: int, b: int) -> int:
    return a * b


def is_even(a: int) -> bool:
    return a % 2 == 0


def sum_equal_to_third(a: int, b: int, c: int) -> bool:
    return a + b == c


def is_number_in_list(lista: list, a: int) -> bool:
    return a in lista


def zad_6(a: list, b: list) -> list:
    return [x ** 3 for x in list(set(a + b))]


def get_breweries() -> list:
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(
        url=url,
        )
    if response.status_code == 200:
        return response.json()
    else:
        return []
