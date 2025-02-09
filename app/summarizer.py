from spitch import Spitch
from openai import OpenAI
from typing import Dict, Optional
import os

class NewsSummarizerWithTTS:
    def __init__(self, openai_key: str, spitch_key: str):
        self.openai_client = OpenAI(api_key=openai_key)
        self.spitch_client = Spitch(api_key=spitch_key)
        
    def summarize_and_speak(self, text: str, language: str = "en", voice: str = "john") -> tuple[Optional[str], Optional[bytes]]:
        summary = self.summarize(text)
        if summary:
            try:
                audio = self.spitch_client.speech.generate(
                    text=summary,
                    language=language,
                    voice=voice
                )
                return summary, audio.read()
            except Exception as e:
                print(f"TTS Error: {e}")
                return summary, None
        return None, None

    def summarize(self, text: str, max_tokens: int = 100) -> Optional[str]:
        try:
            response = self.openai_client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"Summarize the following article in 2-3 sentences:\n\n{text}",
                max_tokens=max_tokens,
                temperature=0.5,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Summarization Error: {e}")
            return None