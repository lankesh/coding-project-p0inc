from src.adapters.calendar import CalendarAdapter, DummyCalendarAdapter
from src.config import config
from src.exceptions.common import CustomException
from src.schemas.request import SetAvailabilityRequest
from src.services.schedule import FindOverlap, GetAvailability, SetAvailability
from src.validators.schedule import SetAvailabilityValidator


def get_calendar_adapter() -> CalendarAdapter:
    adapter_type = config.calendar_adapter
    if adapter_type == "dummy":
        return DummyCalendarAdapter()
    raise CustomException(
        message=(
            f"Invalid adapter type: {adapter_type}. "
            + "Allowed adapter types: ['dummy']"
        ),
        status_code=500,
    )


def build_set_availability_service(request: SetAvailabilityRequest) -> SetAvailability:
    adapter = get_calendar_adapter()
    # Perform validations before returning the service object
    validator = SetAvailabilityValidator(request=request, adapter=adapter)
    validator.validate()
    return SetAvailability(request=request, adapter=adapter)


def build_get_availability_service(user_email: str, date: str) -> GetAvailability:
    adapter = get_calendar_adapter()
    return GetAvailability(adapter=adapter, date=date, user_email=user_email)


def build_find_overlap_service(first_user_email: str, second_user_email: str, date: str) -> FindOverlap:
    adapter = get_calendar_adapter()
    return FindOverlap(
        adapter=adapter,
        date=date,
        first_user_email=first_user_email,
        second_user_email=second_user_email,
    )
