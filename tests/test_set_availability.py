def test_set_availability(client):
    request_body = {
        "user_email": "johndoe@example.com",
        "date": "2024-08-30",
        "start_time": "10:00",
        "end_time": "11:00",
    }
    response = client.post("/schedule/availability/", json=request_body)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["data"] == request_body

def test_invalid_request_body_set_availability(client):
    request_body = {
        "user_email": "johndoe@example.com@sample",
        "date": "2024-08-30 13:30:59",
        "start_time": "10:00:59",
        "end_time": "11:00:59",
    }
    response = client.post("/schedule/availability/", json=request_body)
    assert response.status_code == 422
    response_data = response.json()
    assert "errors" in response_data["data"]
    errors = response_data["data"]["errors"]
    assert len(errors) == 4
    email_error = False
    date_error = False
    start_time_error = False
    end_time_error = False
    for error in errors:
        if error["field"] == "user_email":
            email_error = True
        elif error["field"] == "date":
            date_error = True
        elif error["field"] == "start_time":
            start_time_error = True
        elif error["field"] == "end_time":
            end_time_error = True
    assert email_error and date_error and start_time_error and end_time_error

def test_end_time_smaller_than_start_time_set_availability(client):
    request_body = {
        "user_email": "johndoe@example.com",
        "date": "2024-08-30",
        "start_time": "11:00",
        "end_time": "10:00",
    }
    response = client.post("/schedule/availability/", json=request_body)
    assert response.status_code == 422
    response_data = response.json()
    assert "errors" in response_data["data"]
    errors = response_data["data"]["errors"]
    assert len(errors) == 1
    end_time_error = False
    for error in errors:
        if error["field"] == "end_time":
            end_time_error = True
    assert end_time_error

def test_overlapping_availability_slot_set_availability(client):
    request_body = {
        "user_email": "johndoe@example.com",
        "date": "2024-08-30",
        "start_time": "10:00",
        "end_time": "11:00",
    }
    response = client.post("/schedule/availability/", json=request_body)
    assert response.status_code == 200
    request_body = {
        "user_email": "johndoe@example.com",
        "date": "2024-08-30",
        "start_time": "10:30",
        "end_time": "11:30",
    }
    response = client.post("/schedule/availability/", json=request_body)
    assert response.status_code == 409
    response_data = response.json()
    assert "errors" in response_data["data"]
    errors = response_data["data"]["errors"]
    assert len(errors) == 2
    start_time_error = False
    end_time_error = False
    for error in errors:
        if error["field"] == "start_time":
            start_time_error = True
        elif error["field"] == "end_time":
            end_time_error = True
    assert start_time_error and end_time_error
