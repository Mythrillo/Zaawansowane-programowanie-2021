from models.KlasaAdresowa import KlasaAdresowa


class Magazyn(KlasaAdresowa):

    def __init__(
        self,
        miasto: str,
        ulica: str,
        numer_budynku: int,
        nazwa_magazynu: str,
        typ_sprzetu: str
    ) -> None:
        super().__init__(miasto, ulica, numer_budynku)
        self.nazwa_magazynu = nazwa_magazynu
        self.typ_sprzetu = typ_sprzetu

    def __str__(self) -> str:
        return f"Magazyn {self.nazwa_magazynu} o adresie: {self.miasto} ul.: {self.ulica} {self.numer_budynku} zajmujący się sprzętem typu {self.typ_sprzetu}."

    @property
    def get_nazwa_magazynu(self) -> str:
        return self.nazwa_magazynu

    @property
    def get_typ_sprzetu(self) -> str:
        return self.typ_sprzetu
