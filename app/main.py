from app.news_digest import NewsDigest
from config import CONFIG

def main():
    digest = NewsDigest(CONFIG)
    digest.run()

if __name__ == "__main__":
    main()