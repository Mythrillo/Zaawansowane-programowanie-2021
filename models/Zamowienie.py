from typing import List

from models.Mieszkanie import Mieszkanie
from models.Dom import Dom
from models.Developer import Developer


class Zamowienie:

    def __init__(self) -> None:
        self._mieszkania = None
        self._domy = None
        self._developer = None
        self._data = None

    @property
    def mieszkania(self) -> List[Mieszkanie]:
        return self._mieszkania

    @property
    def domy(self) -> List[Dom]:
        return self._domy

    @property
    def developer(self) -> Developer:
        return self._developer

    @property
    def data(self) -> str:
        return self._data

    @mieszkania.setter
    def mieszkania(self, mieszkania) -> None:
        self._mieszkania = mieszkania

    @domy.setter
    def domy(self, domy) -> None:
        self._domy = domy

    @developer.setter
    def developer(self, developer) -> None:
        self._developer = developer

    @data.setter
    def data(self, data) -> None:
        self._data = data

    def oblicz_wartosc(self) -> float:
        cena = 0
        for mieszkanie in self._mieszkania:
            cena += mieszkanie.cena
        for dom in self._domy:
            cena += dom.cena
        return round(cena, 2)

    def oblicz_metry(self) -> float:
        metry_kwadratowe = 0
        for mieszkanie in self._mieszkania:
            metry_kwadratowe += mieszkanie.pole
        for dom in self._domy:
            metry_kwadratowe += dom.pole
        return metry_kwadratowe

    def __str__(self) -> str:
        return f"""Zamowienie na: {len(self._domy)} domy,
            {len(self._mieszkania)} mieszkania,
            od developera {self._developer}"""
