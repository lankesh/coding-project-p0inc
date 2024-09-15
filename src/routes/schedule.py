from fastapi import APIRouter, Depends

from src.dependencies.calendar import (
    build_get_availability_service,
    build_find_overlap_service,
    build_set_availability_service,
)
from src.exceptions.common import CustomException
from src.services.schedule import (
    FindOverlap,
    GetAvailability,
    SetAvailability,
)
from src.schemas.response import (
    FindOverlapResponseBody,
    FindOverlapResponseBodyData,
    GetAvailabilityResponseBody,
    GetAvailabilityResponseBodyData,
    ValidationFailureResponseBody,
    FailureResponseBody,
    SetAvailabilityResponseBody,
)

router = APIRouter(
    prefix="/schedule",
)


@router.post(
    path="/availability/",
    response_model=SetAvailabilityResponseBody,
    responses={
        422: {
            "description": "Validation Error",
            "model": ValidationFailureResponseBody,
        },
        409: {
            "description": "Overlapping availability slot found",
            "model": FailureResponseBody,
        },
        500: {
            "description": "Internal Server Error",
            "model": FailureResponseBody,
        },
    },
)
async def set_availability(
    service: SetAvailability=Depends(build_set_availability_service),
):
    ret_val = service.save()
    if ret_val:
        return SetAvailabilityResponseBody(
            data=service.request.model_dump(),
        )
    else:
        raise CustomException(
            message="Failed to save availability slot",
            status_code=500,
        )


@router.get(
    path="/availability/{user_email}/{date}",
    response_model=GetAvailabilityResponseBody,
)
async def get_availability(
    service: GetAvailability=Depends(build_get_availability_service),
):
    slots = service.get_slots()
    return GetAvailabilityResponseBody(
        data=GetAvailabilityResponseBodyData(
            user_email=service.user_email,
            date=service.date,
            slots=slots,
        ),
    )


@router.get(
    path="/overlap/{first_user_email}/{second_user_email}/{date}",
    response_model=FindOverlapResponseBody,
)
async def get_overlap(
    service: FindOverlap=Depends(build_find_overlap_service),
):
    slots = service.find_overlap()
    return FindOverlapResponseBody(
        data=FindOverlapResponseBodyData(
            first_user_email=service.first_user_email,
            second_user_email=service.second_user_email,
            date=service.date,
            slots=slots,
        ),
    )
