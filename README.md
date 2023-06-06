# Follower Tracker for Twitter

This simple Python script lets you track who you are following on Twitter but are not following you back. This tool uses the Tweepy library to interact with the Twitter API.

## Requirements
- Python 3.6+
- [Tweepy](https://www.tweepy.org/)

## Setup

1. Download main.py

2. Install dependencies:
```bash
pip install tweepy
```

3. You need to set up Twitter API keys to authenticate with Twitter. You can obtain these keys by applying for a [Twitter Developer account](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and creating an app.

4. Create a new `.env` file in the root directory and add your Twitter API keys:
```env
CONSUMER_KEY='your-consumer-key'
CONSUMER_SECRET='your-consumer-secret'
ACCESS_TOKEN='your-access-token'
ACCESS_TOKEN_SECRET='your-access-token-secret'
```
Replace `'your-consumer-key'`, `'your-consumer-secret'`, `'your-access-token'`, and `'your-access-token-secret'` with your actual Twitter API keys.

## Usage

Run the script by executing the following command:

```bash
python main.py
```

The script will then output a list of user IDs that you are following but aren't following you back. Please note that this list will only contain the user IDs, as the Twitter API commonly deals with user IDs. If you want to convert these to screen names, you'll need to adjust the code accordingly, but be aware that this will count towards your API rate limit.

## Limitations
Twitter API has rate limits. If you are following or have followers in large numbers, you might hit this rate limit. In such a case, you will need to incorporate sleep time in your script to avoid hitting the rate limit.
