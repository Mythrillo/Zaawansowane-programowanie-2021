from models.Property import Property


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
