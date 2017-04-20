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

