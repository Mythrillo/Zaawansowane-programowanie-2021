
class Property:

    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str
    ) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):

    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
        plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"Area: {self.area} Pokoje: {self.rooms} Cena: {self.price} Adres: {self.address} Pole: {self.plot}"


class Flat(Property):

    def __init__(
        self,
        area: float,
        rooms: int,
        price: float,
        address: str,
        floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"Area: {self.area} Pokoje: {self.rooms} Cena: {self.price} Adres: {self.address} Piętro: {self.floor}"


if __name__ == "__main__":
    house = House(15.5, 5, 100000, "Kasztanowa 15 Katowice", 300)
    print(house)
    flat = Flat(15.5, 1, 9999, "Wyborowa 1 Gliwice", 30)
    print(flat)
