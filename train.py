from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

import logging
import multiprocessing
import time
import pandas as pd 
import os 

np.random.seed(7)

# Clear screen 
os.system('cls')

# Panda testing
word_list = []
df = pd.read_csv('clean_sentences.csv')

for i, sentence in enumerate(df['sentence']):
	segmented_words = word_tokenize(sentence)
	word_list.append(segmented_words)

	if i % 10000 == 0:
		print("%d out of %d sentences segmented" % (i, len(df)))

# Clear up memory
del df 

# Logging Parameters
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Word2Vec Parameters (START)

sg = 1 # Use Skip-Gram Model
size = 500 # Dimensionality size of Projection Layer
window = 10 # Window of surrounding words
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

# Give the model name of file
model_name = "w2v_food_unigram_500"

# Save the file after trimming
model.init_sims(replace=True) # Trim down memory size
model.wv.save_word2vec_format(model_name + '.bin', binary=True)