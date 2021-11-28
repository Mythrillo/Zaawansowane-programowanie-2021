from models.Produkt import Produkt
from models.Magazyn import Magazyn
from models.KlientBiznesowy import KlientBiznesowy
from models.KlientDetaliczny import KlientDetaliczny
from models.Zamowienie import Zamowienie


if __name__ == "__main__":
    mag = Magazyn("Gdańsk", "Zakręcona", 1, "Magazyn Testowy", "Audio")
    prod = Produkt("JBL GO", 9.987654, mag, 2, "Głośnik")
    klient_det = KlientDetaliczny("Detal", "Katowice", "Zawilców", 10, mag)
    klient_biz = KlientBiznesowy("Bizn", "Gliwice", "Wojskowa", 20, mag, "Audio")
    zam = Zamowienie()
    zam.ilosc = 10
    zam.klient = klient_det
    zam.magazyn = mag
    zam.produkt = prod
    zam.data = "28.11.2021 11:00"
    print(zam)
