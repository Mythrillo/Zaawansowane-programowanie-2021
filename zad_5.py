
def is_number_in_list(lista: list, a: int) -> bool:
    return a in lista


if __name__ == "__main__":
    print(is_number_in_list([1, 2, 3], 1))
    print(is_number_in_list([1, 2, 3], 5))
