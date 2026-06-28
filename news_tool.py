import feedparser

def get_news(company):

    url = f"https://news.google.com/rss/search?q={company}"

    news = feedparser.parse(url)

    print("\n========== LATEST NEWS ==========")

    if len(news.entries) == 0:
        print("No news found")
        return

    for article in news.entries[:5]:
        print("-", article.title)