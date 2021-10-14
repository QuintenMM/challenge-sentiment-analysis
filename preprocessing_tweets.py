import string
import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer
from emoji_translate.emoji_translate import Translator
from textblob import TextBlob
import swifter

from emot.emo_unicode import EMOTICONS_EMO


def import_tweets(your_show = 'SquidGame'):
    tweets_filtered = pd.read_csv(your_show)
    tweets_filtered = tweets_filtered.iloc[:, 1:]
    tweets_filtered = tweets_filtered[["user", "text"]].drop_duplicates()
    tweets_filtered.reset_index()
    return tweets_filtered


def remove_punct(text):
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text


def tokenization(text):
    text = re.split('\W+', text)
    return text


stopword = nltk.corpus.stopwords.words('english')


def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text


ps = nltk.PorterStemmer()


def stemming(text):
    text = [ps.stem(word) for word in text]
    return text


wn = nltk.WordNetLemmatizer()


def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text


def clean_text(text):
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation])
    text_rc = re.sub('[0-9]+', '', text_lc)
    tokens = re.split('\W+', text_rc)
    text = [ps.stem(word) for word in tokens if word not in stopword]
    return text


emo = Translator(exact_match_only=False, randomize=True)

# tweets_filtered = tweets_filtered.to_string()
tweets_filtered = import_tweets()
tweets_filtered['tweet_punct'] = tweets_filtered['text'].swifter.apply(lambda x: remove_punct(x))
tweets_filtered['tweet_tokenized'] = tweets_filtered['tweet_punct'].swifter.apply(lambda x: tokenization(x.lower()))
tweets_filtered['tweet_nonstop'] = tweets_filtered['tweet_tokenized'].swifter.apply(lambda x: remove_stopwords(x))
tweets_filtered['tweet_stemmed'] = tweets_filtered['tweet_nonstop'].swifter.apply(lambda x: stemming(x))
tweets_filtered['tweet_lemmatized'] = tweets_filtered['tweet_nonstop'].swifter.apply(lambda x: lemmatizer(x))


# tweets_filtered['tweet_emo'] = tweets_filtered['tweet_punct'].swifter.apply(lambda x:emo.emojify(x))
def get_sentiment(column='text'):
    tweets_filtered['sentiment'] = tweets_filtered[column].apply(lambda x: TextBlob(x).sentiment[0])
    tweets_filtered['subject'] = tweets_filtered[column].apply(lambda x: TextBlob(x).sentiment[1])
    tweets_filtered['polarity'] = tweets_filtered['sentiment'].apply(lambda x: 'pos' if x >= 0 else 'neg')
    return tweets_filtered


# df_tokenized['tweet_tokenized'] = [','.join(map(str, l)) for l in tweets_filtered['tweet_tokenized']]



def avg_polarity(df=tweets_filtered, col='polarity'):
    pos = 0
    neg = 0
    for rating in df[col]:
        if rating == 'pos':
            pos += 1
        elif rating == 'neg':
            neg += 1
        else:
            print('no match')
    if pos > neg:
        return(f"{pos} People are positive about your show and {neg} people don't like it ")
    else:
        return(f'{neg} people are not positive about your show but {pos} are')




# # countVectorizer = CountVectorizer(analyzer=clean_text)
# # countVector = countVectorizer.fit_transform(tweets_filtered['text'])
# #
# # # print('{} Number of tweets has {} words'.format(countVector.shape[0], countVector.shape[1]))
# # # print(countVectorizer.get_feature_names())
# #
# # count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names())
