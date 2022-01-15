from models.Budynek import Budynek


class Mieszkanie(Budynek):

    def __init__(
        self,
        pole: float,
        pokoje: int,
        cena: float,
        balkon: bool
    ) -> None:
        super().__init__(pole, pokoje, cena)
        self._balkon = balkon

    @property
    def balkon(self) -> bool:
        return self._balkon

    def __str__(self) -> str:
        tmp = super().__str__()
        tmp += f"\nBalkon: {self._balkon}"
        return tmp
