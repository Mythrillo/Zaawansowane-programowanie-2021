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
