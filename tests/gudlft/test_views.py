from app import app
from gudlft import views
from gudlft.models import load_clubs, load_competitions


class TestViews:

    client = app.test_client()

    def setup_method(self):
        views.competitions = load_competitions('tests/data/test_competitions.json')
        views.clubs = load_clubs('tests/data/test_clubs.json')

    def test_index(self, client):
        sut = client.get('/')
        assert sut.status_code == 200
    
    def test_clubs_points(self, client):
        sut = client.get('/clubs-points')
        assert sut.status_code == 200

    def test_login(self, client, club_fixture):
        data = {"email": club_fixture["email"]}
        sut = client.post('/show-summary', data=data)
        assert sut.status_code == 200

    def test_login_wrong_credential(self, client):
        data = {"email": "toto@mail.com"}
        sut = client.post('/show-summary', data=data, follow_redirects=True)
        assert sut.status_code == 200
        assert 'Unknown or missing mail address.' in sut.data.decode()

    def test_login_no_credential(self, client):
        data = {"email": ""}
        sut = client.post('/show-summary', data=data, follow_redirects=True)
        assert sut.status_code == 200
        assert 'Unknown or missing mail address.' in sut.data.decode()

    def test_book(self, client):
        sut = client.get("/book/Spring%20Festival/Simply%20Lift")
        assert sut.status_code == 200

    def test_purchase_places(self, client, club_fixture, competition_fixture):
        data = {
            "club": club_fixture['name'],
            "competition": competition_fixture['name'],
            "places": 1,
        }
        sut = self.client.post("/purchase-places", data=data)
        assert sut.status_code == 200
        assert 'Great-booking complete!' in sut.data.decode()


    def test_purchase_places_not_enough_places(self, client, club_fixture, competition_low_places_fixture):
        data = {
            "club": club_fixture['name'],
            "competition": competition_low_places_fixture['name'],
            "places": 5,
        }
        sut = self.client.post("/purchase-places", data=data)
        assert sut.status_code == 200
        assert 'Not enough remaining places.' in sut.data.decode()

    def test_purchase_places_not_enough_points(self, client, club_low_points_fixture, competition_fixture):
        data = {
            "club": club_low_points_fixture['name'],
            "competition": competition_fixture['name'],
            "places": 5,
        }
        sut = self.client.post("/purchase-places", data=data)
        assert sut.status_code == 200
        assert 'You do not have enough points.' in sut.data.decode()

    def test_purchase_places_more_than_allowed(self, client, club_fixture, competition_fixture):
        data = {
            "club": club_fixture['name'],
            "competition": competition_fixture['name'],
            "places": 13,
        }
        sut = self.client.post("/purchase-places", data=data)
        assert sut.status_code == 200
        assert f'You cannot book more than {views.MAX_PLACES_PER_CLUB} places.' in sut.data.decode()

    def test_logout(self):
        sut = self.client.get('/logout', follow_redirects=True)
        assert sut.status_code == 200
