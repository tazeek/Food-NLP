from gensim.models import word2vec
from nltk.tokenize import word_tokenize

import logging
import multiprocessing
import time
import pandas as pd 
import os 

# Clear screen 
os.system('cls')

# Data Streaming Class
class Streamer():

	def __iter__(self):

		# Stream the CSV file
		for sentence in pd.read_csv('clean_sentences')['sentence']:
			yield word_tokenize(sentence)


# Create a stream object 
sent_stream = Streamer()

# Logging Parameters
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Word2Vec Parameters (START)

sg = 1 # Use Skip-Gram Model
size = 300 # Dimensionality size of Projection Layer
window = 5 # Window of surrounding words
alpha = 0.025 # Initial learning rate of the Neural Network
min_count = 5 # Minimum Frequency of Words
workers = multiprocessing.cpu_count() # Number of workers
max_vocab_size = 200000 # Maximum number of Unique Words
negative = 10 # Number of words to be drawn for Negative Sampling
sample = 0.001 # Subsampling of frequent words 
hs = 0 # Negative Sampling to be used
iter = 5 # Iterations over corpus. Also called epochs

# Word2Vec Parameters (END)

# Initialize Word2Vec model 
model = Word2Vec(word_list, sg=sg, size=size, window=window, alpha=alpha, 
	min_count=min_count, workers=workers, max_vocab_size=max_vocab_size, 
	hs=hs, iter=iter, sample=sample)

model_name = "w2v_reddit_bigram_300d(FINAL)"