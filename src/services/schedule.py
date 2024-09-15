from typing import List
from src.adapters.calendar import CalendarAdapter
from src.schemas.request import SetAvailabilityRequest

class SetAvailability:
    def __init__(
        self,
        adapter: CalendarAdapter,
        request: SetAvailabilityRequest,
    ) -> None:
        self.adapter = adapter
        self.request = request

    def save(self) -> bool:
        return self.adapter.set_availability(
            user_email=self.request.user_email,
            date_str=self.request.date,
            slot={
                "start_time": self.request.start_time,
                "end_time": self.request.end_time,
            },
        )

class GetAvailability:
    def __init__(
        self,
        adapter: CalendarAdapter,
        date: str,
        user_email: str,
    ) -> None:
        self.adapter = adapter
        self.date = date
        self.user_email = user_email

    def get_slots(self) -> List[dict]:
        return self.adapter.get_availability(
            user_email=self.user_email,
            date_str=self.date,
        )

class FindOverlap:
    def __init__(
        self,
        adapter: CalendarAdapter,
        date: str,
        first_user_email: str,
        second_user_email: str,
    ) -> None:
        self.adapter = adapter
        self.date = date
        self.first_user_email = first_user_email
        self.second_user_email = second_user_email

    def find_overlap(self) -> List[dict]:
        return self.adapter.find_overlap(
            date_str=self.date,
            user1_email=self.first_user_email,
            user2_email=self.second_user_email,
        )
