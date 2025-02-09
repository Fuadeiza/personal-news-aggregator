# Personal News Aggregator (Broadcaster)

An automated system that scrapes news articles, generates audio summaries using AI, and sends them to a WhatsApp group.

## Features

- Scrapes top 5 daily news articles from Sahara Reporters(New platform)
- Generates concise summaries using OpenAI GPT
- Converts summaries to audio using Spitch TTS
- Stores audio files in Google Cloud Storage
- Sends audio summaries to WhatsApp group via Twilio

## Prerequisites

- Python 3.10+
- Google Cloud Platform account
- Twilio account with WhatsApp enabled
- OpenAI API account
- Spitch API account

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd news-audio-digest
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```env
OPENAI_API_KEY=your_openai_key
SPITCH_API_KEY=your_spitch_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
WHATSAPP_FROM_NUMBER=your_twilio_whatsapp_number
WHATSAPP_TO_NUMBER=target_group_id
GCS_BUCKET_NAME=your_gcs_bucket_name
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
```

## Google Cloud Storage Setup

1. Create a new project in Google Cloud Console
2. Create a new storage bucket
3. Create a service account:
   - Go to IAM & Admin > Service Accounts
   - Create new service account
   - Add roles: "Storage Object Viewer" and "Storage Object Creator"
   - Create and download JSON key
4. Configure bucket permissions:
   - Add service account with "Storage Object Creator" and "Storage Object Viewer" roles
   - Make bucket public by adding "allUsers" with "Storage Object Viewer" role

## WhatsApp Group Setup

1. Create WhatsApp group
2. Add Twilio WhatsApp number to group
3. Send a message to Twilio number from group
4. Get group ID from Twilio console
5. Update WHATSAPP_TO_NUMBER in .env with group ID

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Fetch top 5 articles from Sahara Reporters
2. Generate summaries using GPT-3
3. Convert summaries to audio using Spitch
4. Upload audio files to GCS
5. Send audio messages to WhatsApp group

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── scraper.py         # News scraping functionality
│   ├── summarizer.py      # Text summarization and TTS
│   ├── whatsapp_client.py # WhatsApp messaging
│   ├── storage.py         # GCS storage handling
│   └── news_digest.py     # Main orchestration
├── config.py              # Configuration management
├── main.py               # Entry point
└── requirements.txt      # Dependencies
```

## Requirements

```
beautifulsoup4
requests
python-dotenv
openai
twilio
google-cloud-storage
spitch
```
