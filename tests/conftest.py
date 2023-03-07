import pytest

from app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def club_fixture():
    data = {"name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "15",
            }
    return data


@pytest.fixture
def club_wrong_credential_fixture(club_fixture):
    club_fixture["email"] = "toto@mail.com"
    return club_fixture


@pytest.fixture
def club_no_credential_fixture(club_fixture):
    club_fixture["email"] = ""
    return club_fixture


@pytest.fixture
def competition_fixture():
    data = {"name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25",
            }
    return data
