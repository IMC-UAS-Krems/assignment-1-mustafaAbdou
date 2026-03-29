from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from streaming.models.track import Track
    from streaming.models.user import User


class Playlist:

    def __init__(self, playlist_id: str, name: str, owner: User) -> None:
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks: list[Track] = []

    def add_track(self, track: Track) -> None:
        if track not in self.tracks:
            self.tracks.append(track)

    def remove_track(self, track: Track | str) -> None:
        # accepts either a Track object or a track_id string, silently ignores missing
        if isinstance(track, str):
            self.tracks = [t for t in self.tracks if t.track_id != track]
        elif track in self.tracks:
            self.tracks.remove(track)

    def total_duration_seconds(self) -> int:
        return sum(t.duration_seconds for t in self.tracks)

    def __repr__(self) -> str:
        return f"Playlist(id={self.playlist_id!r}, name={self.name!r}, tracks={len(self.tracks)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.playlist_id == other.playlist_id

    def __hash__(self) -> int:
        return hash(self.playlist_id)
