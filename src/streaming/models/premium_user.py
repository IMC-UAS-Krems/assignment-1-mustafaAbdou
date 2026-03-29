from __future__ import annotations

from datetime import date

from streaming.models.user import User


class PremiumUser(User):

    def __init__(self, user_id: str, name: str, age: int, subscription_start: date | None = None) -> None:
        super().__init__(user_id, name, age)
        self.subscription_start = subscription_start
