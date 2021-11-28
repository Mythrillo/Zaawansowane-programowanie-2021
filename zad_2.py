from zad_1 import Student


class Library:

    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str) -> None:
        self.city = city
        self.zip_code = zip_code
        self.street = street
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Biblioteka w miesście: {self.city} {self.zip_code} na ulicy {self.street}. Godziny otwarcia: {self.open_hours}. Telefon: {self.phone}"


class Employee:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Pracownik {self.first_name} {self.last_name}, zatrudniony {self.hire_date}, urodzony {self.birth_date}, zamieszkały w {self.city} {self.zip_code} {self.street}. Telefon: {self.phone}"


class Order:

    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list,
        order_date: str
    ) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        tmp = ""
        for book in self.books:
            tmp += book + " "
        return f"Zamówienie odebrane przez: {self.employee} dla {self.student} na książki: {tmp} dnia {self.order_date}"


class Book:

    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int
    ) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Książka autorstwa: {self.author_name} {self.author_surname} opublikowana: {self.publication_date}. Liczba stron: {self.number_of_pages}. Dostępna w bibliotece: {self.library}"


if __name__ == "__main__":
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
