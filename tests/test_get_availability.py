from src.db import calendar_db

def test_get_availability_exists(client):
    user_email = "johndoe@example.com"
    date_str = "2024-08-30"
    slot1_start_time = "10:00"
    slot1_end_time = "11:00"
    calendar_db.add_slot(
        user_email=user_email,
        date_str=date_str,
        start_time_str=slot1_start_time,
        end_time_str=slot1_end_time,
    )
    slot2_start_time = "11:00"
    slot2_end_time = "12:00"
    calendar_db.add_slot(
        user_email=user_email,
        date_str=date_str,
        start_time_str=slot2_start_time,
        end_time_str=slot2_end_time,
    )
    response = client.get(f"/schedule/availability/{user_email}/{date_str}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "user_email" in response_data["data"] and response_data["data"]["user_email"] == user_email
    )
    assert (
        "date" in response_data["data"] and response_data["data"]["date"] == date_str
    )
    assert (
        "slots" in response_data["data"] and len(response_data["data"]["slots"]) == 2
    )
    slot1_found = False
    slot2_found = False
    for slot in response_data["data"]["slots"]:
        if slot["start_time"] == slot1_start_time and slot["end_time"] == slot1_end_time:
            slot1_found = True
        elif slot["start_time"] == slot2_start_time and slot["end_time"] == slot2_end_time:
            slot2_found = True
    assert slot1_found and slot2_found

def test_get_availability_does_not_exists(client):
    user_email = "johndoe@example.com"
    date_str = "2024-08-30"
    slot1_start_time = "10:00"
    slot1_end_time = "11:00"
    calendar_db.add_slot(
        user_email=user_email,
        date_str=date_str,
        start_time_str=slot1_start_time,
        end_time_str=slot1_end_time,
    )
    slot2_start_time = "11:00"
    slot2_end_time = "12:00"
    calendar_db.add_slot(
        user_email=user_email,
        date_str=date_str,
        start_time_str=slot2_start_time,
        end_time_str=slot2_end_time,
    )
    search_user_email = "janedoe@example.com"
    response = client.get(f"/schedule/availability/{search_user_email}/{date_str}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "user_email" in response_data["data"] and response_data["data"]["user_email"] == search_user_email
    )
    assert (
        "date" in response_data["data"] and response_data["data"]["date"] == date_str
    )
    assert (
        "slots" in response_data["data"] and len(response_data["data"]["slots"]) == 0
    )

def test_get_availability_slot_exists_date_does_not_exists(client):
    user_email = "johndoe@example.com"
    date_str = "2024-08-30"
    slot1_start_time = "10:00"
    slot1_end_time = "11:00"
    calendar_db.add_slot(
        user_email=user_email,
        date_str=date_str,
        start_time_str=slot1_start_time,
        end_time_str=slot1_end_time,
    )
    slot2_start_time = "11:00"
    slot2_end_time = "12:00"
    calendar_db.add_slot(
        user_email=user_email,
        date_str=date_str,
        start_time_str=slot2_start_time,
        end_time_str=slot2_end_time,
    )
    search_date_str = "2024-08-29"
    response = client.get(f"/schedule/availability/{user_email}/{search_date_str}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "user_email" in response_data["data"] and response_data["data"]["user_email"] == user_email
    )
    assert (
        "date" in response_data["data"] and response_data["data"]["date"] == search_date_str
    )
    assert (
        "slots" in response_data["data"] and len(response_data["data"]["slots"]) == 0
    )
