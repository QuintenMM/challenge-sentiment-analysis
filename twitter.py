import tweepy
import pandas as pd
import time

def text_to_dataframe(word, amount):
    auth = tweepy.OAuthHandler(consumer_key_open, consumer_key_private)
    auth.set_access_token(acces_token_open,acces_token_private)
    api = tweepy.API(auth, retry_delay=3)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


    search_word = word + " -filter:retweets"
    tweets = api.search_tweets(q=search_word, lang="en", count=amount)
    users_text = [[tweet.user.screen_name, tweet.text] for tweet in tweets]
    tweet_text = pd.DataFrame(data=(users_text),columns=['user', "text"])
    tweet_text.to_csv(word, mode="a")


def run_tweepy (word='SquidGame', cycles=1 ):
    count = 0
    if count != cycles:
        text_to_dataframe(word, 100)
        time.sleep(1)
        count += 1

