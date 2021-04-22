from bs4 import BeautifulSoup


class Article:
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_html(cls, html_article):
        for link in html_article.find_all("a"):
            if link["class"][0] == "post__title_link":
                title = link.string
                break

        return cls(title)


class HabrPage:
    def __init__(self, filename):
        self._filename = filename

    def posts(self):
        html_doc = open(self._filename, "r")
        soup = BeautifulSoup(html_doc, "html.parser")

        html_articles = soup.find_all("article")

        articles = [Article.from_html(html_article) for html_article in html_articles]

        return articles


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
