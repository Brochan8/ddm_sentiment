pip install tweepy
import pandas as pd
import tweepy
from datetime import datetime, timedelta
import os

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

def authenticate_twitter_app():
    """Authenticate to the Twitter API."""
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def fetch_tweets(api, query, date_initial, date_final, max_tweets=1000):
    """Fetch tweets using Tweepy."""
    tweets_data = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", since=date_initial, until=date_final, tweet_mode='extended').items(max_tweets):
        tweets_data.append([tweet.user.url, tweet.created_at, tweet.id, tweet.full_text, tweet.user.screen_name])
    
    tweets_df = pd.DataFrame(tweets_data, columns=['URL', 'Datetime', 'Tweet Id', 'Text', 'Username'])
    return tweets_df

def save_tweets_to_csv(tweets_df, date_final):
    """Save tweets DataFrame to a CSV file."""
    filename = f'dados-scrapping-{date_final}.csv'
    tweets_df.to_csv(filename, index=False)
    print(f"Tweets saved to {filename}")

def scrapping(date_initial, date_final, keyword):
    api = authenticate_twitter_app()
    tweets_df = fetch_tweets(api, keyword, date_initial, date_final)
    save_tweets_to_csv(tweets_df, date_final)
    return tweets_df

def main():
    start_date = datetime(2021, 10, 1).strftime('%Y-%m-%d')
    end_date = datetime(2021, 12, 30).strftime('%Y-%m-%d')
    keyword = 'digital dementia'
    data_scrapping = scrapping(start_date, end_date, keyword)
    return data_scrapping

if __name__ == "__main__":
    main()
