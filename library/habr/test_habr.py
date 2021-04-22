from bs4 import BeautifulSoup


class Article:
    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

    @classmethod
    def from_html(cls, html_article):
        for link in html_article.find_all("a"):
            if link["class"][0] == "post__title_link":
                title = link.string
                url = link.get("href")
                break

        for div in html_article.find_all("div"):
            if "post__text" in div["class"]:
                content = div.text
                break

        return cls(title=title, url=url, content=content)


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

    def test_posts_url(self):
        # Given
        habrPage = HabrPage("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.url == "https://habr.com/ru/post/553856/"

    def test_posts_content_startswith(self):
        # Given
        habrPage = HabrPage("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.content.startswith("\nЧеловечество использовало оружие с древних времен.")