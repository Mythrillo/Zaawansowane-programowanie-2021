from models.KlientDetaliczny import KlientDetaliczny
from models.Magazyn import Magazyn


class KlientBiznesowy(KlientDetaliczny):

    def __init__(
        self,
        nazwa_firmy: str,
        miasto: str,
        ulica: str,
        numer_budynku: int,
        najblizszy_magazyn: Magazyn,
        typ_firmy: str
    ) -> None:
        super().__init__(
            nazwa_firmy,
            miasto,
            ulica,
            numer_budynku,
            najblizszy_magazyn
        )
        self.typ_firmy = typ_firmy

    def __str__(self) -> str:
        return f"Klient biznesowy {self.nazwa_firmy} typu {self.typ_firmy} o adresie: {self.miasto} ul.: {self.ulica} {self.numer_budynku}" +\
            f"o najbliższym magazynie {self.najblizszy_magazyn.get_nazwa_magazynu}."

    @property
    def get_typ_firmy(self) -> str:
        return self.typ_firmy
