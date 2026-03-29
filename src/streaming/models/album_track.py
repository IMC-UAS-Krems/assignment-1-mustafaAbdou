from __future__ import annotations

from streaming.models.song import Song
from streaming.models.artist import Artist
from streaming.models.album import Album


class AlbumTrack(Song):
    # track_number defines position within the album; album is set by Album.add_track()

    def __init__(
        self,
        track_id: str,
        title: str,
        duration_seconds: int,
        genre: str,
        artist: Artist,
        track_number: int,
        album: Album | None = None,
    ) -> None:
        super().__init__(track_id, title, duration_seconds, genre, artist)
        self.track_number = track_number
        self.album = album
