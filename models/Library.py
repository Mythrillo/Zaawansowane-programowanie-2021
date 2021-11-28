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
