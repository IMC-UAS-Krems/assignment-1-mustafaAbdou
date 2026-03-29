from collections import defaultdict
from datetime import datetime, timedelta

from streaming.models import (
    User, PremiumUser, FamilyMember, CollaborativePlaylist, Song,
)
from streaming.repositories.abstract_repository import AbstractRepository


class AnalyticsController:

    def __init__(self, repo: AbstractRepository) -> None:
        self._repo = repo

    def total_listening_time_minutes(self, start: datetime, end: datetime) -> float:
        return sum(
            (s.duration_listened_minutes()
            for s in self._repo.all_sessions()
            if start <= s.timestamp <= end),
            0.0
        )

    def avg_unique_tracks_per_premium_user(self, days: int = 30) -> float:
        cutoff = datetime.now() - timedelta(days=days)
        premium = [u for u in self._repo.all_users() if isinstance(u, PremiumUser)]
        if not premium:
            return 0.0
        total = sum(
            len({s.track.track_id for s in u.sessions if s.timestamp >= cutoff})
            for u in premium
        )
        return total / len(premium)

    def track_with_most_distinct_listeners(self):
        sessions = self._repo.all_sessions()
        if not sessions:
            return None
        listeners: dict[str, set[str]] = defaultdict(set)
        for s in sessions:
            listeners[s.track.track_id].add(s.user.user_id)
        top = max(listeners, key=lambda tid: len(listeners[tid]))
        return self._repo.get_track(top)

    def avg_session_duration_by_user_type(self) -> list[tuple[str, float]]:
        durations: dict[str, list[int]] = defaultdict(list)
        for s in self._repo.all_sessions():
            durations[type(s.user).__name__].append(s.duration_listened_seconds)
        result = [(t, sum(d) / len(d)) for t, d in durations.items()]
        return sorted(result, key=lambda x: x[1], reverse=True)

    def total_listening_time_underage_sub_users_minutes(self, age_threshold: int = 18) -> float:
        return sum(
            (s.duration_listened_minutes()
            for s in self._repo.all_sessions()
            if isinstance(s.user, FamilyMember) and s.user.age < age_threshold),
            0.0
        )

    def top_artists_by_listening_time(self, n: int = 5) -> list[tuple]:
        time_by_artist: dict[str, float] = defaultdict(float)
        for s in self._repo.all_sessions():
            if isinstance(s.track, Song):
                time_by_artist[s.track.artist.artist_id] += s.duration_listened_minutes()
        ranked = sorted(time_by_artist.items(), key=lambda x: x[1], reverse=True)[:n]
        return [(self._repo.get_artist(aid), mins) for aid, mins in ranked]

    def user_top_genre(self, user_id: str) -> tuple[str, float] | None:
        user = self._repo.get_user(user_id)
        if user is None or not user.sessions:
            return None
        genre_seconds: dict[str, int] = defaultdict(int)
        for s in user.sessions:
            genre_seconds[s.track.genre] += s.duration_listened_seconds
        total = sum(genre_seconds.values())
        top = max(genre_seconds, key=lambda g: genre_seconds[g])
        return (top, genre_seconds[top] / total * 100)

    def collaborative_playlists_with_many_artists(self, threshold: int = 3) -> list[CollaborativePlaylist]:
        result = []
        for pl in self._repo.all_playlists():
            if not isinstance(pl, CollaborativePlaylist):
                continue
            artists = {t.artist.artist_id for t in pl.tracks if isinstance(t, Song)}
            if len(artists) > threshold:
                result.append(pl)
        return result

    def avg_tracks_per_playlist_type(self) -> dict[str, float]:
        standard, collab = [], []
        for pl in self._repo.all_playlists():
            (collab if isinstance(pl, CollaborativePlaylist) else standard).append(len(pl.tracks))
        return {
            "Playlist": sum(standard) / len(standard) if standard else 0.0,
            "CollaborativePlaylist": sum(collab) / len(collab) if collab else 0.0,
        }

    def users_who_completed_albums(self) -> list[tuple[User, list[str]]]:
        albums = [a for a in self._repo.all_albums() if a.tracks]
        result = []
        for user in self._repo.all_users():
            listened = {s.track.track_id for s in user.sessions}
            completed = [a.title for a in albums if a.track_ids().issubset(listened)]
            if completed:
                result.append((user, completed))
        return result
