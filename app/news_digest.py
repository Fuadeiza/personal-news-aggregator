from .scraper import NewsScraper
from .summarizer import NewsSummarizerWithTTS
from .whatsapp_client import WhatsAppClient
from .storage import GCSStorage
import hashlib

class NewsDigest:
    def __init__(self, config: dict):
        self.scraper = NewsScraper(config['base_url'])
        self.summarizer = NewsSummarizerWithTTS(
            config['openai_key'],
            config['spitch_key']
        )
        self.whatsapp = WhatsAppClient(
            config['twilio_account_sid'],
            config['twilio_auth_token'],
            config['whatsapp_from']
        )
        self.storage = GCSStorage(config['gcs_bucket'])
        self.whatsapp_to = config['whatsapp_to']

    def run(self):
        try:
            articles = self.scraper.fetch_articles(limit=5)
            for article in articles:
                summary, audio = self.summarizer.summarize_and_speak(article['content'])
                if audio:
                    # Create unique filename
                    filename = hashlib.md5(article['title'].encode()).hexdigest()[:10] + '.mp3'
                    audio_url = self.storage.upload_audio(audio, filename)
                    
                    if audio_url:
                        self.whatsapp.send_audio(
                            self.whatsapp_to,
                            article['title'],
                            audio_url
                        )
                        print(f"Sent audio summary for: {article['title']}")
        except Exception as e:
            print(f"Error in digest run: {e}")