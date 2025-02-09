import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time

class NewsScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def fetch_articles(self, limit: int = 5) -> List[Dict]:
        articles = []
        try:
            response = self.session.get(self.base_url)
            soup = BeautifulSoup(response.content, "html.parser")

            article_headings = soup.find_all("h2", class_="title is-3")
            article_urls = [self.base_url + heading.find("a")["href"] for heading in article_headings]

            for url in article_urls[:limit]:
                time.sleep(2)  # Respectful delay between requests
                article_response = self.session.get(url)
                article_soup = BeautifulSoup(article_response.content, "html.parser")

                title = article_soup.find("head").find("title").text.strip()
                content = article_soup.find("div", class_="content story").text.strip()
                
                articles.append({
                    "title": title,
                    "url": url,
                    "content": content,
                })
        except Exception as e:
            print(f"Error scraping articles: {e}")
        return articles