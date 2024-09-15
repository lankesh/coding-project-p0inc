from abc import abstractmethod
from typing import List

from src.db import calendar_db
from src.utils.time_util import convert_time_to_str

class CalendarAdapter:
    @abstractmethod
    def set_availability(self, user_email: str, date_str: str, slot: dict) -> bool:
        pass

    @abstractmethod
    def get_availability(self, user_email: str, date_str: str) -> List[dict]:
        pass

    @abstractmethod
    def find_overlap(self, user1_email: str, user2_email: str, date_str: str) -> List[dict]:
        pass


class DummyCalendarAdapter(CalendarAdapter):
    def __init__(self) -> None:
        super().__init__()

    def set_availability(self, user_email: str, date_str: str, slot: dict) -> bool:
        calendar_db.add_slot(
            user_email=user_email,
            date_str=date_str,
            start_time_str=slot['start_time'],
            end_time_str=slot['end_time'],
        )
        return True

    def get_availability(self, user_email: str, date_str: str) -> List[dict]:
        slots = calendar_db.get_slots(user_email=user_email, date_str=date_str)
        return [
            {
                "start_time": convert_time_to_str(slot["start_time"]),
                "end_time": convert_time_to_str(slot["end_time"]),
            }
            for slot in slots
        ]

    def find_overlap(self, user1_email: str, user2_email: str, date_str: str) -> List[dict]:
        schedule1 = calendar_db.get_slots(user1_email,date_str)
        schedule2 = calendar_db.get_slots(user2_email,date_str)
        if not schedule1 or not schedule2:
            return []
        idx1, idx2 = 0, 0
        overlaps = []
        while idx1 < len(schedule1) and idx2 < len(schedule2):
            start1, end1 = schedule1[idx1]["start_time"], schedule1[idx1]["end_time"]
            start2, end2 = schedule2[idx2]["start_time"], schedule2[idx2]["end_time"]
            if start1 < end2 and start2 < end1:  # Check if times overlap
                start = max(start1, start2)
                end = min(end1, end2)
                overlaps.append({
                    "start_time": convert_time_to_str(start),
                    "end_time": convert_time_to_str(end),
                })
            if end1 < end2:
                idx1 += 1
            else:
                idx2 += 1
        return overlaps
