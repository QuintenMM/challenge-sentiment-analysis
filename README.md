As a project i wanted to determain the sentiment people feel when thinking about there favorite show.

To do this I collect tweets with the hastag of there show. I connect to the api and use a small script to check my tokens and after that I collect  100 tweets from a certain topic. I save the username and the tweet itself in a csv file.

I import the csv file and quicley clean it. Sentiment models already exist so I don't have to train my own models. Using TextBlob I generate the sentiment for each tweet.

From the collection of these tweets I can determaine if most people are talking in a positive way or a negative way about the show. Using this I can see what the overal sentiment is with different shows.
