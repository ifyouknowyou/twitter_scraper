import os
import csv
import time
from datetime import datetime
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get bearer token from environment variable
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

if not BEARER_TOKEN:
    raise ValueError("❌ BEARER_TOKEN not found. Please set it in the .env file.")

# Initialize Twitter API client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True
)

# Keywords to search
KEYWORDS = ["cyber security", "information security", "online safety"]
MAX_RESULTS = 100       # Total tweets per keyword per cycle
TWEETS_PER_QUERY = 50   # Tweets per API request

print("🚀 Twitter collection started... (Press CTRL+C to stop)")

while True:
    for keyword in KEYWORDS:
        all_tweets = []
        print(f"\n🔍 Collecting tweets for: '{keyword}' at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        try:
            paginator = tweepy.Paginator(
                client.search_recent_tweets,
                query=f'"{keyword}" lang:en -is:retweet',
                max_results=TWEETS_PER_QUERY,
                tweet_fields=['created_at', 'text', 'author_id']
            )

            for tweet in paginator.flatten(limit=MAX_RESULTS):
                all_tweets.append([tweet.id, tweet.created_at, tweet.text])

            # Save tweets to CSV
            filename = f"{keyword.replace(' ', '_')}_tweets.csv"
            file_exists = os.path.isfile(filename)

            with open(filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(['Tweet_ID', 'Timestamp', 'Text'])
                writer.writerows(all_tweets)

            print(f"✅ Saved {len(all_tweets)} tweets to {filename}")

        except tweepy.TooManyRequests as e:
            reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
            sleep_time = max(reset_time - int(time.time()), 0) + 5
            print(f"⚠️ Rate limit hit. Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)
            continue

        time.sleep(2)  # Small delay between keywords

    print("\n⏳ Cycle complete. Waiting 60 seconds before next run...")
    time.sleep(60)
