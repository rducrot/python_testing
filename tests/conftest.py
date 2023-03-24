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
            "points": "13",
            }
    return data


@pytest.fixture
def club_low_points_fixture(club_fixture):
    club_fixture["name"] = "Not Enough Points"
    return club_fixture


@pytest.fixture
def competition_fixture():
    data = {"name": "Spring Festival",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "25",
            }
    return data


@pytest.fixture
def competition_low_places_fixture(competition_fixture):
    competition_fixture["name"] = "Not Enough Places"
    return competition_fixture
