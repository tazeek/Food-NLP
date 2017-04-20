from gensim.models import word2vec
from nltk.tokenize import word_tokenize

import logging
import multiprocessing
import time
import pandas as pd 
import os 

# Clear screen 
os.system('cls')

# Utilize the full power of the worker threads available
#os.system("taskset -p 0xff %d" % os.getpid())

# Load Dataframe (Replace later with data streamer)
df = pd.read_csv('clean_sentences.csv')

# Testing Word Segmentation
test = df['sentence'][0]
print(test)
print(word_tokenize(test))