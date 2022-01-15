from models.Budynek import Budynek


class Dom(Budynek):

    def __init__(
        self,
        pole: float,
        pokoje: int,
        cena: float,
        pietra: int
    ) -> None:
        super().__init__(pole, pokoje, cena)
        self._pietra = pietra

    @property
    def pietra(self) -> int:
        return self._pietra

    def __str__(self) -> str:
        tmp = super().__str__()
        tmp += f"\nPietra: {self._pietra}"
