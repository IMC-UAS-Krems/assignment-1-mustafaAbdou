from streaming.models.user import User


class FreeUser(User):

    MAX_SKIPS_PER_HOUR = 6

    def __init__(self, user_id: str, name: str, age: int) -> None:
        super().__init__(user_id, name, age)
