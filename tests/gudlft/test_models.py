import gudlft.models


class TestModels:
    def test_load_clubs_return_list(self):
        sut = gudlft.models.load_clubs()
        assert isinstance(sut, list)

    def test_load_competitions_return_list(self):
        sut = gudlft.models.load_competitions()
        assert isinstance(sut, list)
