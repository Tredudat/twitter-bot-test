"""
Twitter Bot Test for tskatetech.com

This script fetches the latest post from the RSS feed of tskatetech.com,
posts a greeting based on the time of day, and shares a link to the latest
blog post on Twitter.

Requirements:
- Python 3.x
- Tweepy library: pip install tweepy
- feedparser library: pip install feedparser
"""

import tweepy
import feedparser
from datetime import datetime

# Twitter API credentials (replace with your actual credentials)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Initialize Tweepy with Twitter API credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to fetch the latest post from the SquareSpace RSS feed
def get_latest_post(rss_url):
    feed = feedparser.parse(rss_url)
    latest_post = feed.entries[0]
    return latest_post.title, latest_post.link

# Function to post a greeting based on the time of day
def post_greeting():
    now = datetime.now()
    current_time = now.hour
    
    if 5 <= current_time < 12:
        greeting = "Good morning! ☀️"
    elif 12 <= current_time < 18:
        greeting = "Good afternoon! 🌞"
    else:
        greeting = "Good evening! 🌙"
    
    try:
        api.update_status(greeting)
        print("Greeting posted successfully.")
    except Exception as e:
        print("An error occurred while posting greeting: ", e)

# Function to share the latest blog post on Twitter
def share_latest_post(rss_url):
    title, link = get_latest_post(rss_url)
    tweet = f"Check out our latest blog post: {title} {link}"
    
    try:
        api.update_status(tweet)
        print("Blog post shared successfully.")
    except Exception as e:
        print("An error occurred while sharing blog post: ", e)

# RSS feed URL of tskatetech.com
rss_url = 'YOUR_SQUARESPACE_RSS_FEED_URL'

# Main function to execute bot actions
def main():
    try:
        post_greeting()  # Post a greeting
        share_latest_post(rss_url)  # Share the latest blog post
    except Exception as e:
        print("An error occurred: ", e)

# Run the main function
if __name__ == "__main__":
    main()
