import streamlit as st
import twitter
import preprocessing_tweets


st.title('What do people think of your show')
your_show = st.text_input("What is your favorite show?",value='SquidGame')
st.title(your_show)

twitter.run_tweepy(your_show, 1)

tweets_filtered = preprocessing_tweets.import_tweets(your_show)

tweets_filtered = preprocessing_tweets.get_sentiment()

st.write(preprocessing_tweets.avg_polarity(tweets_filtered))

