from google.cloud import storage
import os

class GCSStorage:
    def __init__(self, bucket_name: str):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)
    
    def upload_audio(self, audio_data: bytes, filename: str) -> str:
        blob = self.bucket.blob(f"audio/{filename}")
        blob.upload_from_string(audio_data, content_type='audio/mp3')
        return blob.public_url