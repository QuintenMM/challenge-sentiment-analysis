# sentiment analyses on tweets 

As a project i wanted to determain the sentiment people feel when thinking about there favorite show.

To do this I collect tweets with the hastag of there show. I connect to the api and use a small script to check my tokens. After that I collect  100 tweets from a topic they deside on by filling in a hastag. I collect the tweets and usernames and store them in a csv file.

I import the csv file and quickly clean it. Sentiment models already exist so I don't have to train my own model. using NLP I determain the sentiment people have. this is stored as antother value in the dataframe.

From the collection of these tweets I can determaine if most people are talking in a positive way or a negative way about the show. Using this I can see what the overal sentiment is for different shows.

![](https://github.com/QuintenMM/challenge-sentiment-analysis/blob/25ab69400742c0a80a8fa9fad3b9b56c4d3f7741/visuals/Screenshot%20from%202021-10-14%2014-13-23.png)
