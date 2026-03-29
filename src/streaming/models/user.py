from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from streaming.models.session import ListeningSession


class User(ABC):

    def __init__(self, user_id: str, name: str, age: int) -> None:
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions: list[ListeningSession] = []

    def add_session(self, session: ListeningSession) -> None:
        self.sessions.append(session)

    def total_listening_seconds(self) -> int:
        return sum(s.duration_listened_seconds for s in self.sessions)

    def total_listening_minutes(self) -> float:
        return self.total_listening_seconds() / 60.0

    def unique_tracks_listened(self) -> set[str]:
        return {s.track.track_id for s in self.sessions}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.user_id!r}, name={self.name!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash(self.user_id)
