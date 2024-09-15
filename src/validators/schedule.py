from src.adapters.calendar import CalendarAdapter
from src.exceptions.validation import CustomValidationException
from src.schemas.response import ValidationErrorModel
from src.schemas.request import SetAvailabilityRequest
from src.utils.time_util import convert_to_time


class SetAvailabilityValidator:
    def __init__(
        self,
        request: SetAvailabilityRequest,
        adapter: CalendarAdapter,
    ) -> None:
        self.request = request
        self.adapter = adapter

    def validate(self) -> bool:
        user_slots = self.adapter.get_availability(
            user_email=self.request.user_email,
            date_str=self.request.date,
        )
        for slot in user_slots:
            if (
                convert_to_time(slot.get("start_time")) <= convert_to_time(self.request.end_time) and
                convert_to_time(slot.get("end_time")) >= convert_to_time(self.request.start_time)
            ):
                raise CustomValidationException(
                    status_code=409,
                    message="Given availability slot overlaps with existing slot.",
                    errors=[
                        ValidationErrorModel(
                            field="start_time",
                            error=f"Existing slot start time: {slot.get('start_time')}",
                        ),
                        ValidationErrorModel(
                            field="end_time",
                            error=f"Existing slot end time: {slot.get('end_time')}",
                        ),
                    ],
                )
        return True
