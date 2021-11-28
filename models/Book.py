from models.Library import Library


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
