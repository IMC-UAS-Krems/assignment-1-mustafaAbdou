from streaming.models.podcast import Podcast


class InterviewEpisode(Podcast):

    def __init__(
        self,
        track_id: str,
        title: str,
        duration_seconds: int,
        genre: str,
        host: str,
        description: str = "",
        guest: str = "",
    ) -> None:
        super().__init__(track_id, title, duration_seconds, genre, host, description)
        self.guest = guest
