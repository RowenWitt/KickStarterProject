import pickle, json
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Bidirectional


with open('kickXY.pkl', 'rb') as fp:
	base = pickle.load(fp)

strings = [i[-2] for i in base]
Y_train = [i[-1] for i in base]

tok = Tokenizer()

tok.fit_on_texts(texts=strings)

dex = tok.word_index

seqs = tok.texts_to_sequences(strings)
max_features = len(dex.values()) + 1
maxlen = 43

X_train = sequence.pad_sequences(seqs, maxlen)

recons = tok.sequences_to_texts(seqs)

print('building model')

model = Sequential()

model.add(Embedding(input_dim=max_features,
					embeddings_initializer="uniform", output_dim=256))

model.add(LSTM(64, dropout=0.1, return_sequences=False))

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam',
			  metrics=['accuracy'])

print("training")
history = model.fit(X_train, Y_train,
				   batch_size=10,
				   epochs=1,
				   verbose=0,
				   validation_split=0.2)

print(history.history)
print('---')
print(history.summary())