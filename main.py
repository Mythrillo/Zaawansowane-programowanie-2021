from models.Book import Book
from models.Employee import Employee
from models.Flat import Flat
from models.House import House
from models.Library import Library
from models.Order import Order
from models.Property import Property
from models.Student import Student


if __name__ == "__main__":
    student_true = Student("Mikołaj", 99)
    student_false = Student("Tomasz", 1)
    lib1 = Library(
        "Katowice",
        "Kasztana",
        "11-111",
        "8:00-16:00",
        "123456789"
    )
    lib2 = Library(
        "Gliwice",
        "Żołędzia",
        "11-222",
        "9:00-16:00",
        "987654321"
    )

    book1 = Book(
        lib1,
        "17.11.2021",
        "Kasztan",
        "Nudny",
        "69"
    )
    book2 = Book(
        lib1,
        "13.11.2021",
        "Adam",
        "Bogat",
        "1"
    )
    book3 = Book(
        lib1,
        "17.12.2021",
        "Rupert",
        "Kasztanowy",
        "420"
    )
    book4 = Book(
        lib1,
        "13.12.2021",
        "Kasztan",
        "Nudny",
        "11"
    )
    book5 = Book(
        lib2,
        "17.11.2021",
        "Kasztan",
        "Zwariowany",
        "111"
    )

    emp1 = Employee(
        "Kasztan",
        "Kasztanowy",
        "Dzisiaj",
        "Wczoraj",
        "Katowice",
        "Kasztanowa",
        "11-111",
        "123123123"
    )
    emp2 = Employee(
        "Mariola",
        "Mariolkowa",
        "11.11.2021",
        "11.11.1999",
        "Katowice",
        "Mariol",
        "11-111",
        "123141451"
    )
    emp3 = Employee(
        "Wariat",
        "Wariatowy",
        "11.11.2020",
        "11.11.1232",
        "Katowice",
        "Wariatkowa",
        "11-111",
        "9877438281"
    )

    student1 = Student("Mikołaj", 99)
    student2 = Student("Tomasz", 1)
    student3 = Student("Karol", 49)

    ord1 = Order(
        emp2,
        student1,
        ["Lalka"],
        "20.12.2021"
    )
    ord2 = Order(
        emp2,
        student2,
        ["Dziady"],
        "20.10.2021"
    )

    print(ord1)
    print(ord2)
    house = House(15.5, 5, 100000, "Kasztanowa 15 Katowice", 300)
    print(house)
    flat = Flat(15.5, 1, 9999, "Wyborowa 1 Gliwice", 30)
    print(flat)
