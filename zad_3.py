
def is_even(a: int) -> bool:
    return a % 2 == 0


if __name__ == "__main__":
    x = is_even(101)
    if x:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
