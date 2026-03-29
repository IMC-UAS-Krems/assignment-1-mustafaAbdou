from streaming.models.track import Track


class Podcast(Track):

    def __init__(
        self,
        track_id: str,
        title: str,
        duration_seconds: int,
        genre: str,
        host: str,
        description: str = "",
    ) -> None:
        super().__init__(track_id, title, duration_seconds, genre)
        self.host = host
        self.description = description
