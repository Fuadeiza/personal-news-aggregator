from twilio.rest import Client

class WhatsAppClient:
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
    
    def send_audio(self, to_number: str, title: str, audio_url: str) -> None:
        try:
            self.client.messages.create(
                from_=f'whatsapp:{self.from_number}',
                body=f"🎧 {title}",
                media_url=[audio_url],
                to=f'whatsapp:{to_number}'
            )
        except Exception as e:
            print(f"WhatsApp Error: {e}")