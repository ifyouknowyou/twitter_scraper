# twitter_scraper

Description:
..............
A Python script that uses the Twitter API (via Tweepy) to collect recent tweets for specified keywords, automatically handle rate limits, and save results to CSV files. Perfect for researchers, cybersecurity analysts, and OSINT investigators who need continuous tweet collection.


Features:
-------------
- Collect multiple keywords in English
- Save results to keyword-specific CSV files
- Automatically waits when hitting Twitter API rate limits
- Secure API key storage via .env file
- Easy to customize keywords and settings

Requirements:
-------------
- Python 3.8+
- Tweepy library
- python-dotenv library
- Twitter Developer account with Bearer Token

Installation:
-------------
1. Clone the repository or download the files:
   git clone https://github.com/YourUsername/twitter_scraper.git
   cd twitter_scraper

2. Install required Python libraries:
   pip install -r requirements.txt

Setup:
-------------
1. Create a file named `.env` in the project folder.

2. Add your Twitter Bearer Token in the `.env` file:
   BEARER_TOKEN=your_twitter_bearer_token_here

3. Make sure `.env` is NOT uploaded to GitHub (it's in .gitignore).

Usage:
-------------
1. Run the scraper script:
   python scraper.py

2. The script will:
   - Collect tweets for the keywords specified in `scraper.py`
   - Save results in CSV files (one per keyword)
   - Automatically wait if rate limits are reached

3. To stop the scraper:
   Press CTRL + C

Optional Tips:
-------------
- To run in the background on Linux:
  nohup python scraper.py &

- You can add or change keywords by editing the `KEYWORDS` list in `scraper.py`.
- CSV files are appended each run, so old data is preserved.
