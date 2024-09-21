from fastapi import APIRouter, Depends

from src.dependencies.user import (
    build_get_user_profile,
    build_set_user_profile,
)
from src.exceptions.common import CustomException
from src.schemas.response import (
    GetUserProfileResponseBody,
    GetUserProfileResponseBodyData,
    SetUserProfileResponseBody,
    ValidationFailureResponseBody,
    FailureResponseBody,
)
from src.services.user import GetUserProfile, SetUserProfile

router = APIRouter(
    prefix="/user",
)


@router.post(
    path="/profile/",
    response_model=SetUserProfileResponseBody,
    responses={
        422: {
            "description": "Validation Error",
            "model": ValidationFailureResponseBody,
        },
        500: {
            "description": "Internal Server Error",
            "model": FailureResponseBody,
        },
    },
)
async def set_profile(
    service: SetUserProfile=Depends(build_set_user_profile),
):
    ret_val = service.save_profile()
    if ret_val:
        return SetUserProfileResponseBody(
            data=GetUserProfileResponseBodyData(
                **service.request.model_dump()
            ),
        )
    else:
        raise CustomException(
            message="Failed to save user profile",
            status_code=500,
        )


@router.get(
    path="/profile/{user_email}",
    response_model=GetUserProfileResponseBody,
)
async def get_profile(
    service: GetUserProfile=Depends(build_get_user_profile),
):
    profile = service.get_profile()
    return GetUserProfileResponseBody(
        data=GetUserProfileResponseBodyData(
            **profile,
        ) if profile else None,
    )
