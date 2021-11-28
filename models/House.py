from models.Property import Property


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
