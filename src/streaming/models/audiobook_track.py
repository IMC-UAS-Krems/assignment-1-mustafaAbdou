from streaming.models.track import Track


class AudiobookTrack(Track):

    def __init__(
        self,
        track_id: str,
        title: str,
        duration_seconds: int,
        genre: str,
        author: str,
        narrator: str,
    ) -> None:
        super().__init__(track_id, title, duration_seconds, genre)
        self.author = author
        self.narrator = narrator
