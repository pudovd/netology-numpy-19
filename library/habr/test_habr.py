class HabrPage:
    def __init__(self, filename):
        self._filename = filename

    def posts(self):
        pass


class TestHabrPage:
    def test_posts(self):
        # Given
        habrPage = HabrPage('index.html')

        # When
        posts = habrPage.posts()

        # Then
        assert len(posts) > 0
