import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "5l4P7H6IeqKl3vJrqsKhSMjup"
access_secret = "c9GsmLedQiaXb2tDLd71P0ZWke8l2fXLT4ts352WHjX6hbfkBj"
consumer_key = "1298517507960078338-QN6h9woh8iiykbiNz89tBvuVvWsy7V"
consumer_secret = "foEYjHOGcUqgeRiAGwHeY8xyHNj8BjgoQOgeJAvIwOFag"

#twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#Creating an API object
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk',
                           count = 200,
                           include_rts = False,# not including retweets for the moment
                           tweet_mode = 'extended')
#print(tweets)

tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = { 'user': tweet.user.screen_name,
                      'text': text,
                      'favorite_count': tweet.favorite_count,
                      'retweet_count': tweet.retweet_count,
                      'created_at': tweet.created_at
                    }

    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("elon_musk_twitter_data_sample.csv")


