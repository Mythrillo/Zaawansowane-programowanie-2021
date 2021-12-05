
class Rating:

    def __init__(
        self,
        userId: int,
        movieId: int,
        rating: float,
        timestamp: int
    ) -> None:
        self.user_id = userId
        self.movie_id = movieId
        self.rating = rating
        self.timestamp = timestamp

    def __dict__(self) -> dict:
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "rating": self.rating,
            "timestamp": self.timestamp
        }
