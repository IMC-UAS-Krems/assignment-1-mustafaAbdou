from __future__ import annotations

from datetime import datetime

from streaming.models import Track, Artist, Album, User, Playlist, ListeningSession, CollaborativePlaylist
from streaming.repositories.abstract_repository import AbstractRepository
from streaming.repositories.in_memory_repository import InMemoryRepository
from streaming.controllers.platform_controller import PlatformController
from streaming.controllers.analytics_controller import AnalyticsController


class StreamingPlatform:

    def __init__(self, name: str) -> None:
        self.name = name
        self._repo: AbstractRepository = InMemoryRepository()
        self._platform = PlatformController(self._repo)
        self._analytics = AnalyticsController(self._repo)

    def add_track(self, track: Track) -> None:
        self._platform.add_track(track)

    def add_user(self, user: User) -> None:
        self._platform.add_user(user)

    def add_artist(self, artist: Artist) -> None:
        self._platform.add_artist(artist)

    def add_album(self, album: Album) -> None:
        self._platform.add_album(album)

    def add_playlist(self, playlist: Playlist) -> None:
        self._platform.add_playlist(playlist)

    def record_session(self, session: ListeningSession) -> None:
        self._platform.record_session(session)

    def get_track(self, track_id: str) -> Track | None:
        return self._platform.get_track(track_id)

    def get_user(self, user_id: str) -> User | None:
        return self._platform.get_user(user_id)

    def get_artist(self, artist_id: str) -> Artist | None:
        return self._platform.get_artist(artist_id)

    def get_album(self, album_id: str) -> Album | None:
        return self._platform.get_album(album_id)

    def all_users(self) -> list[User]:
        return self._platform.all_users()

    def all_tracks(self) -> list[Track]:
        return self._platform.all_tracks()

    def total_listening_time_minutes(self, start: datetime, end: datetime) -> float:
        return self._analytics.total_listening_time_minutes(start, end)

    def avg_unique_tracks_per_premium_user(self, days: int = 30) -> float:
        return self._analytics.avg_unique_tracks_per_premium_user(days)

    def track_with_most_distinct_listeners(self) -> Track | None:
        return self._analytics.track_with_most_distinct_listeners()

    def avg_session_duration_by_user_type(self) -> list[tuple[str, float]]:
        return self._analytics.avg_session_duration_by_user_type()

    def total_listening_time_underage_sub_users_minutes(self, age_threshold: int = 18) -> float:
        return self._analytics.total_listening_time_underage_sub_users_minutes(age_threshold)

    def top_artists_by_listening_time(self, n: int = 5) -> list[tuple[Artist, float]]:
        return self._analytics.top_artists_by_listening_time(n)

    def user_top_genre(self, user_id: str) -> tuple[str, float] | None:
        return self._analytics.user_top_genre(user_id)

    def collaborative_playlists_with_many_artists(self, threshold: int = 3) -> list[CollaborativePlaylist]:
        return self._analytics.collaborative_playlists_with_many_artists(threshold)

    def avg_tracks_per_playlist_type(self) -> dict[str, float]:
        return self._analytics.avg_tracks_per_playlist_type()

    def users_who_completed_albums(self) -> list[tuple[User, list[str]]]:
        return self._analytics.users_who_completed_albums()
