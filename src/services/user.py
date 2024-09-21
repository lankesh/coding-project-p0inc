from src.db import user_profile_db
from src.schemas.request import SetUserProfileRequest

class SetUserProfile:
    def __init__(
        self,
        request: SetUserProfileRequest,
    ) -> None:
        self.request = request

    def save_profile(self) -> bool:
        user_profile_db.upsert_user_profile(self.request.model_dump())
        return True

class GetUserProfile:
    def __init__(
        self,
        user_email: str,
    ) -> None:
        self.user_email = user_email

    def get_profile(self) -> dict:
        return user_profile_db.get_user_profile(self.user_email)
