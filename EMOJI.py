# %% [code]
import math
from keras.models import Sequential
from gensim.models.keyedvectors import KeyedVectors
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding
from keras.layers.wrappers import Bidirectional
from keras.layers import LSTM
from keras.layers import Dense
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# %% [code]

root = "/home/joydipb/Documents/CMT309_Comp_DS/emoji_prediction"
train_data = pd.read_csv(root/"us_train.text",
                         sep='delimiter', header=None)
train_data.columns = ["tweets"]
train_labels = pd.read_csv(root/"us_train.labels",
                           sep='delimiter', header=None)
train_tweets = train_data['tweets'].astype(str).values.tolist()

# %% [code]

# %% [code]

train_data["labels"] = train_labels
train_data

# %% [code]

test_data = pd.read_csv(root/"us_test.text", sep='delimiter', header=None)
test_data.columns = ["tweets"]
test_labels = pd.read_csv(root/"us_test.labels",
                          sep='delimiter', header=None)
test_tweets = test_data['tweets'].astype(str).values.tolist()

# %% [code]

test_data["labels"] = test_labels
test_data

# %% [code]

dev = pd.read_csv(root/"us_dev.text", sep='delimiter', header=None)
dev.columns = ["tweets"]
dev_labels = pd.read_csv(root/"us_dev.labels",
                         sep='delimiter', header=None)
dev_tweets = dev['tweets'].astype(str).values.tolist()

# %% [code]

dev["labels"] = dev_labels
dev

# %% [code]

# print the shapes of all files
train_data.shape, test_data.shape  # , mappings.shape

# %% [code]

train_length = train_data.shape[0]
test_length = test_data.shape[0]
train_length, test_length

# %% [code]

nltk.download('stopwords')

# %% [code]

stop_words = stopwords.words("english")
stop_words[:5]

# %% [code]

# tokenize the sentences


def tokenize(tweets):
    stop_words = stopwords.words("english")
    tokenized_tweets = []
    for tweet in tweets:
        # split all words in the tweet
        words = tweet.split(" ")
        tokenized_string = ""
        for word in words:
            # remove @handles -> useless -> no information
            if word[0] != '@' and word not in stop_words:
                # if a hashtag, remove # -> adds no new information
                if word[0] == "#":
                    word = word[1:]
                tokenized_string += word + " "
        tokenized_tweets.append(tokenized_string)
    return tokenized_tweets

# %% [code]

# translate tweets to a sequence of numbers


def encod_tweets(tweets):
    tokenizer = Tokenizer(
        filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', split=" ", lower=True)
    tokenizer.fit_on_texts(tweets)
    return tokenizer, tokenizer.texts_to_sequences(tweets)

# %% [code]

# apply padding to dataset and convert labels to bitmaps


def format_data(encoded_tweets, max_length, labels):
    x = pad_sequences(encoded_tweets, maxlen=max_length, padding='post')
    y = []
    for emoji in labels:
        bit_vec = np.zeros(20)
        bit_vec[emoji] = 1
        y.append(bit_vec)
    y = np.asarray(y)
    return x, y

# %% [code]

# create weight matrix from pre trained embeddings


def create_weight_matrix(vocab, raw_embeddings):
    vocab_size = len(vocab) + 1
    weight_matrix = np.zeros((vocab_size, 300))
    for word, idx in vocab.items():
        if word in raw_embeddings:
            weight_matrix[idx] = raw_embeddings[word]
    return weight_matrix

# %% [code]

# final model


def final_model(weight_matrix, vocab_size, max_length, x, y, epochs=5):
    embedding_layer = Embedding(vocab_size, 300, weights=[
                                weight_matrix], input_length=max_length, trainable=True, mask_zero=True)
    model = Sequential()
    model.add(embedding_layer)
    model.add(Bidirectional(LSTM(128, dropout=0.2, return_sequences=True)))
    model.add(Bidirectional(LSTM(128, dropout=0.2)))
    model.add(Dense(20, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.fit(x, y, epochs=epochs, validation_split=0.25)
    score, acc = model.evaluate(x_test, y_test)
    return model, score, acc


# %% [code]
tokenized_tweets = tokenize(train_data['tweets'])
tokenized_tweets += tokenize(test_data['tweets'])
max_length = math.ceil(sum([len(s.split(" "))
                       for s in tokenized_tweets])/len(tokenized_tweets))
tokenizer, encoded_tweets = encod_tweets(tokenized_tweets)
max_length, len(tokenized_tweets)

# %% [code]

x, y = format_data(encoded_tweets[:train_length],
                   max_length, train_data['labels'])
len(x), len(y)

x_test, y_test = format_data(
    encoded_tweets[train_length:], max_length, test_data['labels'])
len(x_test), len(y_test)

vocab = tokenizer.word_index
vocab, len(vocab)


# %% [code]

! wget https: // nlp.stanford.edu/data/glove.6B.zip

# %% [code]

! unzip glove*.zip

# %% [code]

# load the GloVe vectors in a dictionary:
embeddings_index = {}
#f = open('/kaggle/input/glove840b300dtxt/glove.840B.300d.txt','r',encoding='utf-8')
f = open('glove.6B.100d.txt', 'r', encoding='utf-8')
for line in f:
    values = line.split(' ')
    word = values[0]
    coefs = np.asarray([float(val) for val in values[1:]])
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))

# %% [code]
# create weight matrix from pre trained embeddings
weight_matrix =  create_weight_matrix(vocab, embeddings_index)
len(weight_matrix) 


# %%
