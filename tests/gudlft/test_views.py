from app import app


class TestViews:
    client = app.test_client()

    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_login(self, client, club_fixture):
        data = {"email": club_fixture["email"]}
        response = client.post('/show-summary', data=data)
        assert response.status_code == 200

    def test_login_wrong_credential(self, client, club_wrong_credential_fixture):
        data = {"email": club_wrong_credential_fixture["email"]}
        response = client.post('/show-summary', data=data, follow_redirects=True)
        assert response.status_code == 200

    def test_login_no_credential(self, client, club_no_credential_fixture):
        data = {"email": club_no_credential_fixture["email"]}
        response = client.post('/show-summary', data=data, follow_redirects=True)
        assert response.status_code == 200

    def test_purchase_places(self, client, club_fixture, competition_fixture):
        data = {
            "club": club_fixture['name'],
            "competition": competition_fixture['name'],
            "places": 1,
        }
        response = self.client.post("/purchase-places", data=data, follow_redirects=True)
        assert response.status_code == 200

    def test_purchase_places_not_enough_places(self, client, club_fixture, competition_fixture):
        pass

    def test_purchase_places_not_enough_points(self, client, club_fixture, competition_fixture):
        pass

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        assert response.status_code == 200
