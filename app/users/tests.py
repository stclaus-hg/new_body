from fastapi.testclient import TestClient

from app.main import app
from app.users.schemas import User, Sex


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_user_model():
    user_data = {
        "name": "John Doe",
        "sex": Sex.male.value,
        "password": "12345",
        "email": "john@example.com",
        "is_teacher": True
    }
    user = User(**user_data)
    user.save()
    assert user.name == "John Doe"
    assert user.sex == Sex.male
    assert user.password == "12345"
    assert user.email == "john@example.com"
    assert user.is_teacher


def _test_signup_user():
    user_data = {
        "name": "John Doe",
        "sex": Sex.male.value,
        "password1": "12345",
        "password2": "12345",
        "email": "john@example.com"
    }
    response = client.post("/user/sign-up", user_data)
    assert response.status_code == 200
    assert response.json() == {
        "msg": "User was created successful. Please check you email to "
        "confirm the email addres john@example.com"
    }
