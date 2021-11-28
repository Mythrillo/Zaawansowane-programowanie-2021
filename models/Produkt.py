from models.Magazyn import Magazyn


class Produkt:

    def __init__(
        self,
        nazwa: str,
        cena: float,
        magazyn: Magazyn,
        ilosc: int,
        typ: str
    ) -> None:
        self.nazwa = nazwa
        self.cena = cena
        self.magazyn = magazyn
        self.ilosc = ilosc
        self.typ = typ

    def __str__(self) -> str:
        return f"Produkt: {self.nazwa} typu {self.typ} o cenie {self.cena} za sztukę. Na magazynie {self.magazyn.get_nazwa_magazynu} znajduję się go {self.ilosc}."

    @property
    def get_nazwa(self) -> str:
        return self.nazwa

    @property
    def get_cena(self) -> float:
        return self.cena

    @property
    def get_magazyn(self) -> Magazyn:
        return self.magazyn

    @property
    def get_ilosc(self) -> int:
        return self.ilosc

    @property
    def get_typ(self) -> str:
        return self.typ
