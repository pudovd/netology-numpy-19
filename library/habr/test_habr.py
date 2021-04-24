from lib import HabrPage, Article


class TestHabrPage:
    def test_posts_count(self):
        # Given
        habrPage = HabrPage.from_filename("index.html")

        # When
        posts = habrPage.posts()

        # Then
        assert len(posts) == 20

    def test_posts_title(self):
        # Given
        habrPage = HabrPage.from_filename("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.title == "Кибероружие. Реально ли?"

    def test_posts_url(self):
        # Given
        habrPage = HabrPage.from_filename("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.url == "https://habr.com/ru/post/553856/"

    def test_posts_time(self):
        # Given
        habrPage = HabrPage.from_filename("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.time == "сегодня в 21:25"

    def test_posts_content_startswith(self):
        # Given
        habrPage = HabrPage.from_filename("index.html")

        # When
        post = habrPage.posts()[0]

        # Then
        assert post.content.startswith(
            "\nЧеловечество использовало оружие с древних времен."
        )

    def test_posts_find_by_keyword(self):
        # Given
        habrPage = HabrPage.from_filename("index.html")
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
