from streaming.models import Track, Artist, Album, User, Playlist, ListeningSession
from streaming.repositories.abstract_repository import AbstractRepository


class PlatformController:

    def __init__(self, repo: AbstractRepository) -> None:
        self._repo = repo

    def add_track(self, track: Track) -> None:
        self._repo.add_track(track)

    def get_track(self, track_id: str) -> Track | None:
        return self._repo.get_track(track_id)

    def all_tracks(self) -> list[Track]:
        return self._repo.all_tracks()

    def add_user(self, user: User) -> None:
        self._repo.add_user(user)

    def get_user(self, user_id: str) -> User | None:
        return self._repo.get_user(user_id)

    def all_users(self) -> list[User]:
        return self._repo.all_users()

    def add_artist(self, artist: Artist) -> None:
        self._repo.add_artist(artist)

    def get_artist(self, artist_id: str) -> Artist | None:
        return self._repo.get_artist(artist_id)

    def add_album(self, album: Album) -> None:
        self._repo.add_album(album)

    def get_album(self, album_id: str) -> Album | None:
        return self._repo.get_album(album_id)

    def add_playlist(self, playlist: Playlist) -> None:
        self._repo.add_playlist(playlist)

    def record_session(self, session: ListeningSession) -> None:
        # push to both the user's own list and the global session store
        session.user.add_session(session)
        self._repo.add_session(session)
