
def hello(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


if __name__ == "__main__":
    x = hello("Mikołaj", "Kałuża")
    print(x)
