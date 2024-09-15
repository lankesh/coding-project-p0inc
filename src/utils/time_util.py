from datetime import time

def convert_to_time(time_str: str) -> time:
    hours, minutes = map(int, time_str.split(':'))
    return time(hours, minutes)

def convert_time_to_str(time_: time) -> str:
    return time_.strftime("%H:%M")
