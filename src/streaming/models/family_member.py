from streaming.models.user import User
from streaming.models.family_account_user import FamilyAccountUser


class FamilyMember(User):

    def __init__(self, user_id: str, name: str, age: int, parent: FamilyAccountUser) -> None:
        super().__init__(user_id, name, age)
        self.parent = parent
