from streaming.models.podcast import Podcast


class NarrativeEpisode(Podcast):

    def __init__(
        self,
        track_id: str,
        title: str,
        duration_seconds: int,
        genre: str,
        host: str,
        description: str = "",
        season: int = 1,
        episode_number: int = 1,
    ) -> None:
        super().__init__(track_id, title, duration_seconds, genre, host, description)
        self.season = season
        self.episode_number = episode_number
