def test_set_user_profile(client):
    request_body = {
        "email": "johndoe@example.com",
        "name": "John Doe",
    }
    response = client.post("/user/profile/", json=request_body)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["data"] == request_body

def test_set_user_profile_422(client):
    request_body = {
        "user_email": "johndoe@example.com",
        "name": "John Doe",
    }
    response = client.post("/user/profile/", json=request_body)
    assert response.status_code == 422
    response_data = response.json()
    assert "errors" in response_data["data"]
    assert len(response_data["data"]["errors"]) == 1
    assert "field" in response_data["data"]["errors"][0]
    assert response_data["data"]["errors"][0]["field"] == "email"
