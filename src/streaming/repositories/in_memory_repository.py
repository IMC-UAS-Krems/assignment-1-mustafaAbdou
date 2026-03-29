from streaming.models import (
    Track, Artist, Album, User, Playlist, ListeningSession,
)
from streaming.repositories.abstract_repository import AbstractRepository


class InMemoryRepository(AbstractRepository):

    def __init__(self) -> None:
        self._tracks: dict[str, Track] = {}
        self._users: dict[str, User] = {}
        self._artists: dict[str, Artist] = {}
        self._albums: dict[str, Album] = {}
        self._playlists: dict[str, Playlist] = {}
        self._sessions: list[ListeningSession] = []

    def add_track(self, track: Track) -> None:
        self._tracks[track.track_id] = track

    def get_track(self, track_id: str) -> Track | None:
        return self._tracks.get(track_id)

    def all_tracks(self) -> list[Track]:
        return list(self._tracks.values())

    def add_user(self, user: User) -> None:
        self._users[user.user_id] = user

    def get_user(self, user_id: str) -> User | None:
        return self._users.get(user_id)

    def all_users(self) -> list[User]:
        return list(self._users.values())

    def add_artist(self, artist: Artist) -> None:
        self._artists[artist.artist_id] = artist

    def get_artist(self, artist_id: str) -> Artist | None:
        return self._artists.get(artist_id)

    def all_artists(self) -> list[Artist]:
        return list(self._artists.values())

    def add_album(self, album: Album) -> None:
        self._albums[album.album_id] = album

    def get_album(self, album_id: str) -> Album | None:
        return self._albums.get(album_id)

    def all_albums(self) -> list[Album]:
        return list(self._albums.values())

    def add_playlist(self, playlist: Playlist) -> None:
        self._playlists[playlist.playlist_id] = playlist

    def get_playlist(self, playlist_id: str) -> Playlist | None:
        return self._playlists.get(playlist_id)

    def all_playlists(self) -> list[Playlist]:
        return list(self._playlists.values())

    def add_session(self, session: ListeningSession) -> None:
        self._sessions.append(session)

    def all_sessions(self) -> list[ListeningSession]:
        return list(self._sessions)
