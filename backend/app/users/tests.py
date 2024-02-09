from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.users.schemas import UserCreate, Sex
from app.users import crud

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_signup_user():
    user_data = {
        "name": "John Doe",
        "sex": "male",
        "password": "12345",
        "re_password": "12345",
        "email": "john@example.com",
        "is_coach": False
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data


def test_create_user(db: Session):
    user_data = {
        "name": "John Doe",
        "sex": Sex.male,
        "password": "12345",
        "hashed_password": "12345fakehashed",
        "email": "john@example.com"
    }
    user_in = UserCreate(
        name=user_data["name"],
        sex=Sex.male,
        email=user_data["email"],
        password=user_data["password"],
        re_password=user_data["password"]
    )
    user = crud.create_user(db, user_in=user_in)

    assert user.email == "john@example.com"
    assert user.hashed_password == user_data['hashed_password']
    assert user.sex == user_data["sex"]
    assert user.name == user_data["name"]
