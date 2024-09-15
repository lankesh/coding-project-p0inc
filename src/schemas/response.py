from typing import Any, List
from pydantic import BaseModel, EmailStr


class ResponseBodyBase(BaseModel):
    success: bool
    data: Any

class SuccessResponseBody(BaseModel):
    success: bool = True

class SetAvailabilityResposeData(BaseModel):
    user_email: EmailStr
    date: str
    start_time: str
    end_time: str

class SetAvailabilityResponseBody(SuccessResponseBody):
    data: SetAvailabilityResposeData

class GetAvailabilityResponseBodyData(BaseModel):
    user_email: EmailStr
    date: str
    slots: List[dict]

class GetAvailabilityResponseBody(SuccessResponseBody):
    data: GetAvailabilityResponseBodyData

class FindOverlapResponseBodyData(BaseModel):
    first_user_email: EmailStr
    second_user_email: EmailStr
    date: str
    slots: List[dict]

class FindOverlapResponseBody(SuccessResponseBody):
    data: FindOverlapResponseBodyData

class ValidationErrorModel(BaseModel):
    field: str
    error: str

class FailureResponseBodyData(BaseModel):
    errors: List[ValidationErrorModel]

class FailureResponseBody(BaseModel):
    success: bool = False
    message: str = ""
    data: None

class ValidationFailureResponseBody(FailureResponseBody):
    data: FailureResponseBodyData
