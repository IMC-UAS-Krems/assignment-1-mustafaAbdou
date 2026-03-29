from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from streaming.models.track import Track


class Artist:

    def __init__(self, artist_id: str, name: str, genre: str) -> None:
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
        self.tracks: list[Track] = []

    def add_track(self, track: Track) -> None:
        self.tracks.append(track)

    def track_ids(self) -> set[str]:
        return {t.track_id for t in self.tracks}

    def track_count(self) -> int:
        return len(self.tracks)

    def duration_seconds(self) -> int:
        return sum(t.duration_seconds for t in self.tracks)

    def __repr__(self) -> str:
        return f"Artist(id={self.artist_id!r}, name={self.name!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Artist):
            return NotImplemented
        return self.artist_id == other.artist_id

    def __hash__(self) -> int:
        return hash(self.artist_id)
