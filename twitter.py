import tweepy
import pandas as pd
import time

def text_to_dataframe(word, amount):
    auth = tweepy.OAuthHandler("M6pe373Psy5FOwSOL6Q6cW3OQ", "KnDkgsgk8wFPVha21KdEOfKYJ6kYoIzUlkoABJSwavUbqadvO3")
    auth.set_access_token("1447465814182010881-3fo5PLwFfO6vlr3BywZEDaAu39WkJy","ZWtza699mka6sH9vo5OghrRwFEFzEgzvEgVloiniAninP")
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

