from models.Magazyn import Magazyn
from models.KlasaAdresowa import KlasaAdresowa


class KlientDetaliczny(KlasaAdresowa):

    def __init__(
        self,
        nazwa_firmy: str,
        miasto: str,
        ulica: str,
        numer_budynku: int,
        najblizszy_magazyn: Magazyn
    ) -> None:
        super().__init__(miasto, ulica, numer_budynku)
        self.nazwa_firmy = nazwa_firmy
        self.najblizszy_magazyn = najblizszy_magazyn

    def __str__(self) -> str:
        return f"Klient detaliczny {self.nazwa_firmy} o adresie: {self.miasto} ul.: {self.ulica} {self.numer_budynku} o najbliższym magazynie {self.najblizszy_magazyn.get_nazwa_magazynu}."

    @property
    def get_nazwa_firmy(self) -> str:
        return self.nazwa_firmy

    @property
    def get_najblizszy_magazyn(self) -> str:
        return self.najblizszy_magazyn
