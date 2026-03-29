from datetime import date

from streaming.models.song import Song
from streaming.models.artist import Artist


class SingleRelease(Song):

    def __init__(
        self,
        track_id: str,
        title: str,
        duration_seconds: int,
        genre: str,
        artist: Artist,
        release_date: date,
    ) -> None:
        super().__init__(track_id, title, duration_seconds, genre, artist)
        self.release_date = release_date
