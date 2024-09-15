
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.exceptions.common import CustomException
from src.exceptions.validation import CustomValidationException
from src.schemas.response import (
    FailureResponseBody,
    ValidationFailureResponseBody,
    FailureResponseBodyData,
    ValidationErrorModel,
)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Transform validation errors into a list of dictionaries with just the field name and error message
    errors = [
        # {
        #     "field": ".".join(map(str, err['loc'][-1:])),  # Take the last element of 'loc' as the field name
        #     "error": err['msg']  # Error message
        # }
        ValidationErrorModel(
            field=".".join(map(str, err['loc'][-1:])),  # Take the last element of 'loc' as the field name
            error=err['msg'],  # Error message
        )
        for err in exc.errors()
    ]
    # Custom response structure
    return JSONResponse(
        status_code=422,
        content=ValidationFailureResponseBody(
            message="There were validation errors in your request.",
            data=FailureResponseBodyData(
                errors=errors,
            ),
        ).model_dump(),
    )

async def custom_validation_exception_handler(request: Request, exc: CustomValidationException):
    # Transform validation errors into a list of dictionaries with just the field name and error message
    return JSONResponse(
        status_code=exc.status_code,
        content=ValidationFailureResponseBody(
            message=str(exc),
            data=FailureResponseBodyData(
                errors=exc.errors,
            ),
        ).model_dump(),
    )

async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content=FailureResponseBody(
            message=str(exc),
            data=None,
        ).model_dump(),
    )
