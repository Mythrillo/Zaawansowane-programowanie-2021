
class Movie:

    def __init__(
        self,
        movieId: int,
        title: str,
        genres: str
    ) -> None:
        self.id = movieId
        self.title = title
        self.genres = genres

    def __dict__(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "genres": self.genres
        }
