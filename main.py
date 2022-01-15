from models.Dom import Dom
from models.Zamowienie import Zamowienie
from models.Mieszkanie import Mieszkanie
from models.Developer import Developer


if __name__ == "__main__":
    domek = Dom(100, 5, 2000, 1)
    mieszkanie = Mieszkanie(60.5423, 3, 1234.5678, True)
    developer = Developer("Budowlaniec", [mieszkanie], [domek], "budo@budowlaniec.com")
    zamowienie = Zamowienie()
    zamowienie.domy = [domek]
    zamowienie.mieszkania = [mieszkanie]
    zamowienie.developer = developer
    zamowienie.data = "15.01.2022"
    print(zamowienie)
