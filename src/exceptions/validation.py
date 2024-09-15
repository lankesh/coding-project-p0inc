from typing import List

from src.exceptions.common import CustomException
from src.schemas.response import ValidationErrorModel


class CustomValidationException(CustomException):
    def __init__(
        self,
        message: str,
        status_code: int,
        errors: List[ValidationErrorModel]=[],
    ) -> None:
        super().__init__(message=message, status_code=status_code)
        self.errors: List[ValidationErrorModel] = errors
