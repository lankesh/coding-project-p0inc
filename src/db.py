from typing import Dict, List, Optional

from src.utils.time_util import convert_to_time

class CalendarDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # data is of type: Dict[str, Dict[str, List[Dict]]]
            # e.g. of record:
            #    data = {"johndoe@example.com":{"2024-12-31":[{"start_time":"11:00","end_time":"12:00"}]}}
            cls._instance.data = {}
        return cls._instance

    def add_slot(self, user_email: str, date_str: str, start_time_str: str, end_time_str: str):
        start_time = convert_to_time(start_time_str)
        end_time = convert_to_time(end_time_str)
        if user_email not in self.data:
            self.data[user_email] = {}
        if date_str not in self.data[user_email]:
            self.data[user_email][date_str] = []
        self.data[user_email][date_str].append({"start_time": start_time, "end_time": end_time})

    def get_slots(self, user_email: str, date_str: str) -> List[Dict]:
        if (
            user_email not in self.data
        ) or (
            date_str not in self.data.get(user_email)
        ):
            return []
        return sorted(self.data[user_email][date_str], key=lambda slot: slot['start_time'])

    def reset(self):
        self.data.clear()


calendar_db = CalendarDatabase()

class UserProfileDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # data is of type: Dict[str, Dict]
            # e.g. of record:
            #    data = {"johndoe@example.com":{"name": "John Doe", "address": "New York"}
            cls._instance.data = {}
        return cls._instance

    def upsert_user_profile(self, user_details: dict):
        email = user_details.get("email")
        if not email:
            raise Exception("email attribute is required")
        self.data[email] = user_details

    def get_user_profile(self, user_email: str) -> Optional[dict]:
        return self.data.get(user_email)

    def reset(self):
        self.data.clear()


user_profile_db = UserProfileDatabase()
