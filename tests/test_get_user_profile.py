from src.db import user_profile_db

def test_get_user_profile_exists(client):
    user_profile = {
        "email": "johndoe@example.com",
        "name": "John Doe",
    }
    user_profile_db.upsert_user_profile(user_profile)
    response = client.get(f"/user/profile/{user_profile['email']}")
    assert response.status_code == 200
    response_data = response.json()
    assert (
        "email" in response_data["data"] and response_data["data"]["email"] == user_profile['email']
    )
    assert (
        "name" in response_data["data"] and response_data["data"]["name"] == "John Doe"
    )

def test_get_user_profile_does_not_exists(client):
    user_profile = {
        "email": "johndoe@example.com",
        "name": "John Doe"
    }
    user_profile_db.upsert_user_profile(user_profile)
    search_user_email = "janedoe@example.com"
    response = client.get(f"/user/profile/{search_user_email}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["data"] is None
