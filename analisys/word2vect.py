import pandas as pd
import numpy as np
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import gensim
import os
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten, LSTM, GRU
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.initializers import Constant
from keras.layers.embeddings import Embedding
from gensim.models import Word2Vec
import pickle
from analisys.makecsv import makecsv

# ---------preprocessdata


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
def main():
    # makecsv()

    df = pd.DataFrame()
    df = pd.read_csv('analisys/movie_data.csv', encoding='utf-8')
    review_lines = list()
    lines = df['review'].values.tolist()

    for line in lines:
        tokens = word_tokenize(line)
        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        review_lines.append(words)

    EMBEDDING_DIM = 100
    # train word2vec model
    model = gensim.models.Word2Vec(sentences=review_lines, size=EMBEDDING_DIM, window=5, workers=4, min_count=1)
    # vocab size
    words = list(model.wv.vocab)

    # save model in ASCII (word2vec) format
    filename = 'imdb_embedding_word2vec.txt'
    model.wv.save_word2vec_format(filename, binary=False)

    embeddings_index = {}
    f = open(os.path.join('', 'imdb_embedding_word2vec.txt'), encoding="utf-8")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:])
        embeddings_index[word] = coefs
    f.close()

    X_train = df.loc[:24999, 'review'].values
    y_train = df.loc[:24999, 'sentiment'].values
    X_test = df.loc[25000:, 'review'].values
    y_test = df.loc[25000:, 'sentiment'].values

    total_reviews = X_train + X_test

    max_length = 35  # try other options like mean of sentence lengths

    VALIDATION_SPLIT = 0.2

    # vectorize the text samples into a 2D integer tensor
    tokenizer_obj = Tokenizer()
    tokenizer_obj.fit_on_texts(review_lines)
    sequences = tokenizer_obj.texts_to_sequences(review_lines)

    # pad sequences
    word_index = tokenizer_obj.word_index

    review_pad = pad_sequences(sequences, maxlen=max_length)
    sentiment = df['sentiment'].values

    # split the data into a training set and a validation set
    indices = np.arange(review_pad.shape[0])
    np.random.shuffle(indices)
    review_pad = review_pad[indices]
    sentiment = sentiment[indices]
    num_validation_samples = int(VALIDATION_SPLIT * review_pad.shape[0])

    X_train_pad = review_pad[:-num_validation_samples]
    y_train = sentiment[:-num_validation_samples]
    X_test_pad = review_pad[-num_validation_samples:]
    y_test = sentiment[-num_validation_samples:]

    num_words = len(word_index) + 1
    embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))

    for word, i in word_index.items():
        if i > num_words:
            continue
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            # words not found in embedding index will be all-zeros.
            embedding_matrix[i] = embedding_vector

    # define model
    model = Sequential()
    # load pre-trained word embeddings into an Embedding layer
    # note that we set trainable = False so as to keep the embeddings fixed
    embedding_layer = Embedding(num_words,
                                EMBEDDING_DIM,
                                embeddings_initializer=Constant(embedding_matrix),
                                input_length=max_length,
                                trainable=False)

    model.add(embedding_layer)
    model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    # compile network
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit the model
    model.fit(X_train_pad, y_train, batch_size=128, epochs=25, validation_data=(X_test_pad, y_test), verbose=2)

    # define model
    model = Sequential()
    embedding_layer = Embedding(num_words,
                                EMBEDDING_DIM,
                                embeddings_initializer=Constant(embedding_matrix),
                                input_length=max_length,
                                trainable=False)
    model.add(embedding_layer)
    model.add(GRU(units=32, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))

    # try using different optimizers and different optimizer configs
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train_pad, y_train, batch_size=128, epochs=25, validation_data=(X_test_pad, y_test), verbose=2)

    score, acc = model.evaluate(X_test_pad, y_test, batch_size=128)

    print('Test score:', score)
    print('Test accuracy:', acc)

    print("Accuracy: {0:.2%}".format(acc))


    #save model and token
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer_obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


    model.save("model.h5")

if __name__ == '__main__':
    main()