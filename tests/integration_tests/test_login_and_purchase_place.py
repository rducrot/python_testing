from app import app
from gudlft import views
from gudlft.models import load_clubs, load_competitions


class TestLoginAndPurchasePlace:

    client = app.test_client()

    def setup_class(self):
        views.competitions = load_competitions('tests/data/test_competitions.json')
        views.clubs = load_clubs('tests/data/test_clubs.json')

    def test_login_and_purchase_place(self, client, club_fixture, competition_fixture):
        login = {"email": club_fixture["email"]}
        login_response = client.post('/show-summary', data=login)
        assert login_response.status_code == 200
        assert f'Welcome, {club_fixture["email"]}' in login_response.data.decode()

        data = {
            "club": club_fixture['name'],
            "competition": competition_fixture['name'],
            "places": 1,
        }
        response = client.post('/purchase-places', data=data)

        assert response.status_code == 200
        assert "Great-booking complete!" in response.data.decode()

        expected_points = int(club_fixture['points']) - 1
        assert f"Points available: {expected_points}" in response.data.decode()

        expected_places = int(competition_fixture['numberOfPlaces']) - 1
        assert f"{competition_fixture['name']}<br />\n            "\
               f"Date: {competition_fixture['date']}<br />\n            "\
               f"Number of Places: {expected_places}" in response.data.decode()

        logout_response = client.get('/logout', follow_redirects=True)
        assert logout_response.status_code == 200
