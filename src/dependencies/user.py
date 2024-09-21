from pydantic import EmailStr
from src.schemas.request import SetUserProfileRequest
from src.services.user import GetUserProfile, SetUserProfile


def build_set_user_profile(request: SetUserProfileRequest) -> SetUserProfile:
    return SetUserProfile(request=request)

def build_get_user_profile(user_email: EmailStr) -> GetUserProfile:
    return GetUserProfile(user_email=user_email)
