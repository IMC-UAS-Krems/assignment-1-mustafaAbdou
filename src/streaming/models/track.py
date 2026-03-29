from abc import ABC


class Track(ABC):

    def __init__(self, track_id: str, title: str, duration_seconds: int, genre: str) -> None:
        self.track_id = track_id
        self.title = title
        self.duration_seconds = duration_seconds
        self.genre = genre

    def duration_minutes(self) -> float:
        return self.duration_seconds / 60.0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.track_id!r}, title={self.title!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Track):
            return NotImplemented
        return self.track_id == other.track_id

    def __hash__(self) -> int:
        return hash(self.track_id)
