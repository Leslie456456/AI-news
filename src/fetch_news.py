import feedparser


class NewsAggregator:
    def __init__(self):
        self.sources = [
            {
                "name": "FDA News",
                "url": "https://www.fda.gov/news-events/fda-newsroom/rss.xml"
            },
            {
                "name": "STAT News",
                "url": "https://www.statnews.com/feed/"
            },
            {
                "name": "Nature",
                "url": "https://www.nature.com/nature.rss"
            },
            {
                "name": "arXiv AI",
                "url": "http://export.arxiv.org/rss/cs.AI"
            },
            {
                "name": "medRxiv",
                "url": "https://www.medrxiv.org/rss/latest.xml"
            },
        ]

        self.keywords = [
            "artificial intelligence",
            "AI",
            "machine learning",
            "large language model",
            "LLM",
            "agent",
            "healthcare",
            "medicine",
            "FDA",
            "regulatory",
            "pharma",
            "drug safety",
            "pharmacovigilance",
            "clinical trial",
            "real-world evidence",
            "RWE",
        ]

    def fetch_all_news(self):
        articles = []

        for source in self.sources:
            print(f"Fetching from {source['name']}...")
            feed = feedparser.parse(source["url"])

            for entry in feed.entries[:10]:
                title = entry.get("title", "")
                link = entry.get("link", "")
                summary = entry.get("summary", "")

                text = f"{title} {summary}".lower()

                if any(keyword.lower() in text for keyword in self.keywords):
                    articles.append({
                        "title": title,
                        "link": link,
                        "summary": summary,
                        "source": source["name"]
                    })

        # remove duplicate titles
        seen = set()
        unique_articles = []

        for article in articles:
            if article["title"] not in seen:
                unique_articles.append(article)
                seen.add(article["title"])

        return unique_articles[:10]
