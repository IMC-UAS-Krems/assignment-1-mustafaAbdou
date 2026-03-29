from __future__ import annotations

from typing import TYPE_CHECKING

from streaming.models.playlist import Playlist

if TYPE_CHECKING:
    from streaming.models.user import User


class CollaborativePlaylist(Playlist):

    def __init__(self, playlist_id: str, name: str, owner: User) -> None:
        super().__init__(playlist_id, name, owner)
        self.contributors: list[User] = [owner]

    def add_contributor(self, user: User) -> None:
        if user not in self.contributors:
            self.contributors.append(user)

    def remove_contributor(self, user: User) -> None:
        # owner can never be removed
        if user is self.owner:
            return
        self.contributors.remove(user)

    def __repr__(self) -> str:
        return (
            f"CollaborativePlaylist(id={self.playlist_id!r}, name={self.name!r}, "
            f"contributors={len(self.contributors)}, tracks={len(self.tracks)})"
        )
