from abc import ABC, abstractmethod

from streaming.models import (
    Track, Artist, Album, User, Playlist, ListeningSession,
)


class AbstractRepository(ABC):

    @abstractmethod
    def add_track(self, track: Track) -> None: ...

    @abstractmethod
    def get_track(self, track_id: str) -> Track | None: ...

    @abstractmethod
    def all_tracks(self) -> list[Track]: ...

    @abstractmethod
    def add_user(self, user: User) -> None: ...

    @abstractmethod
    def get_user(self, user_id: str) -> User | None: ...

    @abstractmethod
    def all_users(self) -> list[User]: ...

    @abstractmethod
    def add_artist(self, artist: Artist) -> None: ...

    @abstractmethod
    def get_artist(self, artist_id: str) -> Artist | None: ...

    @abstractmethod
    def all_artists(self) -> list[Artist]: ...

    @abstractmethod
    def add_album(self, album: Album) -> None: ...

    @abstractmethod
    def get_album(self, album_id: str) -> Album | None: ...

    @abstractmethod
    def all_albums(self) -> list[Album]: ...

    @abstractmethod
    def add_playlist(self, playlist: Playlist) -> None: ...

    @abstractmethod
    def get_playlist(self, playlist_id: str) -> Playlist | None: ...

    @abstractmethod
    def all_playlists(self) -> list[Playlist]: ...

    @abstractmethod
    def add_session(self, session: ListeningSession) -> None: ...

    @abstractmethod
    def all_sessions(self) -> list[ListeningSession]: ...
