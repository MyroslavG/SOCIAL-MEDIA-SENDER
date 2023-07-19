import tweepy
import facebook as fb 
import requests

# Twitter
client = tweepy.Client(consumer_key="YOUR TWITTER CONSUMER KEY",
                    consumer_secret="YOUR TWITTER SECRET CONSUMER KEY",
                    access_token="YOUR TWITTER ACCESS TOKEN",
                    access_token_secret="YOUR TWITTER SECRET ACCESS TOKEN")
response = client.create_tweet(text='YOUR TWEET HERE')

# Facebook
access_token = 'YOUR META ACCESS TOKEN'
asafb = fb.GraphAPI(access_token)
asafb.put_object('me', 'feed', message = "YOUR TEXT HERE")

# TikTok
#soon

# Instagram
#soon
