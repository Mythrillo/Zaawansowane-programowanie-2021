

class Budynek:

    def __init__(
        self,
        pole: float,
        pokoje: int,
        cena: float
    ) -> None:
        self._pole = pole
        self._pokoje = pokoje
        self._cena = cena

    @property
    def pole(self) -> float:
        return self._pole

    @property
    def pokoje(self) -> int:
        return self._pokoje

    @property
    def cena(self) -> float:
        return self._cena

    def __str__(self) -> str:
        return f"""Pole: {self._pole}
        Pokoje: {self._pokoje}
        Cena: {self._cena}"""
