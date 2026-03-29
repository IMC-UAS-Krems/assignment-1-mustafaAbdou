from streaming.models.track import Track
from streaming.models.artist import Artist


class Song(Track):

    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str, artist: Artist) -> None:
        super().__init__(track_id, title, duration_seconds, genre)
        self.artist = artist
