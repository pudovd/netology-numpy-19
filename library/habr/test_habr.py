from bs4 import BeautifulSoup


class Article:
    def __init__(self, title, url, time, content):
        self.title = title
        self.url = url
        self.time = time
        self.content = content

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.url == other.url
            and self.time == other.time
            and self.content[:10] == other.content[:10]
        )

    def __repr__(self):
        return f'Article(title={self.title}, url={self.url}, time={self.time}, content={self.content}'

    @classmethod
    def from_html(cls, html_article):
        for link in html_article.find_all("a"):
            if "post__title_link" in link["class"]:
                title = link.string
                url = link.get("href")
                break

        for span in html_article.find_all("span"):
            if "post__time" in span["class"]:
                time = span.text
                break

        for div in html_article.find_all("div"):
            if "post__text" in div["class"]:
                content = div.text
                break

        return cls(title=title, url=url, time=time, content=content)

    def has_keywords(self, keywords):
        for keyword in keywords:
            if keyword in self.title.lower() or keyword in self.content.lower():
                return True

        return False


class HabrPage:
    def __init__(self, filename):
        self._filename = filename

    def posts(self):
        html_doc = open(self._filename, "r")
        soup = BeautifulSoup(html_doc, "html.parser")

        html_articles = soup.find_all("article")

        articles = [Article.from_html(html_article) for html_article in html_articles]

        return articles

    def find_by_keywords(self, keywords):
        return [post for post in self.posts() if post.has_keywords(keywords)]


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

    def test_posts_time(self):
        # Given
        habrPage = HabrPage("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.time == "сегодня в 21:25"

    def test_posts_content_startswith(self):
        # Given
        habrPage = HabrPage("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.content.startswith(
            "\nЧеловечество использовало оружие с древних времен."
        )

    def test_posts_find_by_keyword(self):
        # Given
        habrPage = HabrPage("index.html")
        keywords = ["python"]

        # When
        expected_posts = [
            Article(
                title="Бесшовная интеграция Microsoft Excel и Word с помощью Python",
                url="https://habr.com/ru/company/skillfactory/blog/553224/",
                time="сегодня в 16:02",
                content="\nХотя в среднем для каждодневных задач автоматизация не требуется",
            )
        ]
        actual_posts = habrPage.find_by_keywords(keywords)

        # Then
        assert expected_posts == actual_posts
