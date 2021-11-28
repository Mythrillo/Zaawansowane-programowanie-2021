from models.Produkt import Produkt
from models.KlientBiznesowy import KlientBiznesowy
from models.KlientDetaliczny import KlientDetaliczny
from models.Magazyn import Magazyn


class Zamowienie:

    def __init__(self) -> None:
        self.ilosc = None
        self.data = None
        self.produkt = None
        self.magazyn = None
        self.klient = None

    def __str__(self) -> str:
        return f"Zamówienie dla {self.klient.get_nazwa_firmy} w ilości {self.ilosc} w dniu {self.data}." +\
            f"Zamówiony produkt {self.produkt.get_nazwa} z magazynu {self.magazyn.get_nazwa_magazynu} na adres {self.adres_klienta()}." +\
            f"Łączny koszt sprzętu: {self.oblicz_koszt_zamowienia()}"

    @property
    def get_klient(self) -> KlientDetaliczny or KlientBiznesowy:
        return self.klient

    @property
    def get_ilosc(self) -> int:
        return self.ilosc

    @property
    def get_produkt(self) -> Produkt:
        return self.produkt

    @property
    def get_data(self) -> str:
        return self.data

    @property
    def get_magazyn(self) -> Magazyn:
        return self.magazyn

    @get_magazyn.setter
    def get_magazyn(self, magazyn: Magazyn) -> None:
        self.magazyn = magazyn

    @get_klient.setter
    def get_klient(self, klient: KlientBiznesowy or KlientDetaliczny) -> None:
        self.klient = klient

    @get_ilosc.setter
    def get_ilosc(self, ilosc: int) -> None:
        self.ilosc = ilosc

    @get_produkt.setter
    def get_produkt(self, produkt: Produkt) -> None:
        self.produkt = produkt

    @get_data.setter
    def get_data(self, data: str) -> None:
        self.data = data

    def oblicz_koszt_zamowienia(self):
        return round(self.ilosc * self.produkt.get_cena, 2)

    def adres_klienta(self):
        return f"{self.klient.get_miasto} {self.klient.get_ulica} {self.klient.get_numer_budynku}"
