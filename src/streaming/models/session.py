from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from streaming.models.user import User
    from streaming.models.track import Track


class ListeningSession:

    def __init__(
        self,
        session_id: str,
        user: User,
        track: Track,
        timestamp: datetime,
        duration_listened_seconds: int,
    ) -> None:
        self.session_id = session_id
        self.user = user
        self.track = track
        self.timestamp = timestamp
        self.duration_listened_seconds = duration_listened_seconds

    def duration_listened_minutes(self) -> float:
        return self.duration_listened_seconds / 60.0

    def __repr__(self) -> str:
        return (
            f"ListeningSession(id={self.session_id!r}, user={self.user.user_id!r}, "
            f"track={self.track.track_id!r}, duration={self.duration_listened_seconds}s)"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListeningSession):
            return NotImplemented
        return self.session_id == other.session_id

    def __hash__(self) -> int:
        return hash(self.session_id)
