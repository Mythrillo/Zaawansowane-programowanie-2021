
class Link:

    def __init__(
        self,
        movieId: int,
        imdbId: str,
        tmdbId: int
    ) -> None:
        self.movie_id = movieId
        self.imdb_id = imdbId
        self.tmdb_id = tmdbId

    def __dict__(self) -> dict:
        return {
            "movie_id": self.movie_id,
            "imdb_id": self.imdb_id,
            "tmdb_id": self.tmdb_id
        }
