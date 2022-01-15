from typing import List

from models.Mieszkanie import Mieszkanie
from models.Dom import Dom


class Developer:

    def __init__(
        self,
        nazwa_firmy: str,
        mieszkania: List[Mieszkanie],
        domy: List[Dom],
        email: str
    ) -> None:
        self._nazwa_firmy = nazwa_firmy
        self._mieszkania = mieszkania
        self._domy = domy
        self._email = email

    @property
    def nazwa_firmy(self) -> str:
        return self._nazwa_firmy

    @property
    def mieszkania(self) -> List[Mieszkanie]:
        return self._mieszkania

    @property
    def email(self) -> str:
        return self._email

    @property
    def domy(self) -> List[Dom]:
        return self._domy

    def __str__(self) -> str:
        return f"""{self._nazwa_firmy} posiadający:
            {len(self._mieszkania)} mieszkania,
            {len(self._domy)} domy.
            Email kontatkowy: {self._email}"""
