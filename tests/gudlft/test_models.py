import gudlft.models


class TestModels:
    def test_load_clubs_return_list(self):
        sut = gudlft.models.load_clubs('tests/data/test_clubs.json')
        assert isinstance(sut, list)

    def test_load_competitions_return_list(self):
        sut = gudlft.models.load_competitions('tests/data/test_competitions.json')
        assert isinstance(sut, list)
