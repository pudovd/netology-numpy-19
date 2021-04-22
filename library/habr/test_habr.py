from bs4 import BeautifulSoup


class HabrPage:
    def __init__(self, filename):
        self._filename = filename

    def posts(self):
        html_doc = open(self._filename, "r")
        soup = BeautifulSoup(html_doc, "html.parser")

        html_articles = soup.find_all("article")

        return html_articles


class TestHabrPage:
    def test_posts_count(self):
        # Given
        habrPage = HabrPage("index.html")

        # When
        posts = habrPage.posts()

        # Then
        assert len(posts) == 20

    def test_posts_title(self):
        # Given
        habrPage = HabrPage("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.title == "Кибероружие. Реально ли?"
