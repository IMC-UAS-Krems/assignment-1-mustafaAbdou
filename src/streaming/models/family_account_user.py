from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from streaming.models.premium_user import PremiumUser

if TYPE_CHECKING:
    from streaming.models.family_member import FamilyMember


class FamilyAccountUser(PremiumUser):

    def __init__(self, user_id: str, name: str, age: int, subscription_start: date | None = None) -> None:
        super().__init__(user_id, name, age, subscription_start)
        self.sub_users: list[FamilyMember] = []

    def add_sub_user(self, sub_user: FamilyMember) -> None:
        self.sub_users.append(sub_user)

    def all_members(self) -> list:
        return [self] + list(self.sub_users)
