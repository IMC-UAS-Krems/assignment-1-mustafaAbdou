from __future__ import annotations

from typing import TYPE_CHECKING

from streaming.models.artist import Artist

if TYPE_CHECKING:
    from streaming.models.album_track import AlbumTrack


class Album:

    def __init__(self, album_id: str, title: str, artist: Artist, release_year: int) -> None:
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks: list[AlbumTrack] = []

    def add_track(self, track: AlbumTrack) -> None:
        track.album = self
        self.tracks.append(track)
        self.tracks.sort(key=lambda t: t.track_number)

    def track_ids(self) -> set[str]:
        return {t.track_id for t in self.tracks}

    def duration_seconds(self) -> int:
        return sum(t.duration_seconds for t in self.tracks)

    def __repr__(self) -> str:
        return f"Album(id={self.album_id!r}, title={self.title!r}, tracks={len(self.tracks)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Album):
            return NotImplemented
        return self.album_id == other.album_id

    def __hash__(self) -> int:
        return hash(self.album_id)
