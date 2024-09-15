from datetime import datetime, time
from pydantic import (
    BaseModel,
    EmailStr,
    ValidationInfo,
    field_validator,
)
import re


class SetAvailabilityRequest(BaseModel):
    user_email: EmailStr
    date: str
    start_time: str
    end_time: str

    @field_validator('start_time', 'end_time')
    def validate_time_format(cls, value):
        # Validate HH:MM format using regex
        if not re.match(r'^\d{2}:\d{2}$', value):
            raise ValueError('Time must be in HH:MM format. E.g. time: 16:00')
        try:
            return value
        except ValueError:
            raise ValueError("Invalid time format")

    @field_validator("date")
    def validate_date(cls, value):
        # Validate that 'date' is in YYYY-MM-DD (e.g. 2024-12-31) format
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format. E.g. date: 2024-12-31.")

    @field_validator('end_time')
    def check_time_order(cls, end_time, values: ValidationInfo):
        # Validate that 'end_time' is always after 'start_time'
        _start_time = time.fromisoformat(values.data.get('start_time'))
        _end_time = time.fromisoformat(end_time)
        if _start_time and _end_time <= _start_time:
            raise ValueError('end_time must be after start_time')
        return end_time
