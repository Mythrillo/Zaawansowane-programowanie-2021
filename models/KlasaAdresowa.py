class KlasaAdresowa:

    def __init__(
        self,
        miasto: str,
        ulica: str,
        numer_budynku: int
    ) -> None:
        self.miasto = miasto
        self.ulica = ulica
        self.numer_budynku = numer_budynku

    @property
    def get_miasto(self) -> str:
        return self.miasto

    @property
    def get_ulica(self) -> str:
        return self.ulica

    @property
    def get_numer_budynku(self) -> int:
        return self.numer_budynku
