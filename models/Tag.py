
class Tag:

    def __init__(
        self,
        userId: int,
        movieId: int,
        tag: str,
        timestamp: int
    ) -> None:
        self.user_id = userId
        self.movie_id = movieId
        self.tag = tag
        self.timestamp = timestamp

    def __dict__(self) -> dict:
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "tag": self.tag,
            "timestamp": self.timestamp
        }
