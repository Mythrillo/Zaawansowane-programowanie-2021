class Student:

    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50

    def __str__(self) -> str:
        return f"Student: {self.name} z punktami: {self.marks}"
