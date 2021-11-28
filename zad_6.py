
def zad_6(a: list, b: list) -> list:
    return [x ** 3 for x in list(set(a + b))]


if __name__ == "__main__":
    print(zad_6([1, 2, 3], [1, 2, 3]))
    print(zad_6([1, 2, 3], [1, 2, 3, 4]))
