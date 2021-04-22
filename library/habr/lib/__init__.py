from bs4 import BeautifulSoup


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