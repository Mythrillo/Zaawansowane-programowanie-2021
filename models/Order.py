from models.Student import Student
from models.Employee import Employee


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
