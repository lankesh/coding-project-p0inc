from src.db import calendar_db

def test_find_overlap_exists(client):
    date_str = "2024-08-30"
    first_user_email = "johndoe@example.com"
    slot1_start_time = "10:00"
    slot1_end_time = "11:00"
    calendar_db.add_slot(
        user_email=first_user_email,
        date_str=date_str,
        start_time_str=slot1_start_time,
        end_time_str=slot1_end_time,
    )
    second_user_email = "janedoe@example.com"
    slot2_start_time = "10:30"
    slot2_end_time = "11:30"
    calendar_db.add_slot(
        user_email=second_user_email,
        date_str=date_str,
        start_time_str=slot2_start_time,
        end_time_str=slot2_end_time,
    )
    response = client.get(f"/schedule/overlap/{first_user_email}/{second_user_email}/{date_str}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "first_user_email" in response_data["data"] and response_data["data"]["first_user_email"] == first_user_email
    )
    assert (
        "second_user_email" in response_data["data"] and response_data["data"]["second_user_email"] == second_user_email
    )
    assert (
        "date" in response_data["data"] and response_data["data"]["date"] == date_str
    )
    assert (
        "slots" in response_data["data"] and len(response_data["data"]["slots"]) == 1
    )
    overlap_slot_found = False
    for slot in response_data["data"]["slots"]:
        # This checkes for start_time = 10:30 and end_time = 11:00 slot
        if slot["start_time"] == slot2_start_time and slot["end_time"] == slot1_end_time:
            overlap_slot_found = True
    assert overlap_slot_found

def test_find_overlap_multiple_exists(client):
    date_str = "2024-08-30"
    first_user_email = "johndoe@example.com"
    slot1_start_time = "10:00"
    slot1_end_time = "11:00"
    calendar_db.add_slot(
        user_email=first_user_email,
        date_str=date_str,
        start_time_str=slot1_start_time,
        end_time_str=slot1_end_time,
    )
    second_user_email = "janedoe@example.com"
    slot2_start_time = "10:30"
    slot2_end_time = "11:30"
    calendar_db.add_slot(
        user_email=second_user_email,
        date_str=date_str,
        start_time_str=slot2_start_time,
        end_time_str=slot2_end_time,
    )
    slot3_start_time = "09:30"
    slot3_end_time = "10:30"
    calendar_db.add_slot(
        user_email=second_user_email,
        date_str=date_str,
        start_time_str=slot3_start_time,
        end_time_str=slot3_end_time,
    )
    response = client.get(f"/schedule/overlap/{first_user_email}/{second_user_email}/{date_str}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "first_user_email" in response_data["data"] and response_data["data"]["first_user_email"] == first_user_email
    )
    assert (
        "second_user_email" in response_data["data"] and response_data["data"]["second_user_email"] == second_user_email
    )
    assert (
        "date" in response_data["data"] and response_data["data"]["date"] == date_str
    )
    assert (
        "slots" in response_data["data"] and len(response_data["data"]["slots"]) == 2
    )
    overlap_slot1_found = False
    overlap_slot2_found = False
    for slot in response_data["data"]["slots"]:
        # This checkes for start_time = 10:30 and end_time = 11:00 slot
        if slot["start_time"] == slot2_start_time and slot["end_time"] == slot1_end_time:
            overlap_slot1_found = True
        # This checkes for start_time = 10:00 and end_time = 10:30 slot
        if slot["start_time"] == slot1_start_time and slot["end_time"] == slot3_end_time:
            overlap_slot2_found = True
    assert overlap_slot1_found and overlap_slot2_found

def test_find_overlap_does_not_exists(client):
    date_str = "2024-08-30"
    first_user_email = "johndoe@example.com"
    slot1_start_time = "10:00"
    slot1_end_time = "11:00"
    calendar_db.add_slot(
        user_email=first_user_email,
        date_str=date_str,
        start_time_str=slot1_start_time,
        end_time_str=slot1_end_time,
    )
    second_user_email = "janedoe@example.com"
    slot2_start_time = "11:30"
    slot2_end_time = "12:30"
    calendar_db.add_slot(
        user_email=second_user_email,
        date_str=date_str,
        start_time_str=slot2_start_time,
        end_time_str=slot2_end_time,
    )
    response = client.get(f"/schedule/overlap/{first_user_email}/{second_user_email}/{date_str}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "first_user_email" in response_data["data"] and response_data["data"]["first_user_email"] == first_user_email
    )
    assert (
        "second_user_email" in response_data["data"] and response_data["data"]["second_user_email"] == second_user_email
    )
    assert (
        "date" in response_data["data"] and response_data["data"]["date"] == date_str
    )
    assert (
        "slots" in response_data["data"] and len(response_data["data"]["slots"]) == 0
    )
