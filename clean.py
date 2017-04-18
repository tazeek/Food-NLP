import pandas as pd 
import numpy as np 
import re
import codecs
import time
import os
import itertools


# Read the csv file
reviews_df = pd.read_csv('Reviews.csv')

# Array to store comments
clean_reviews = []

# Loop through comments in 'Text' tag
for i in range(0, 20):
    print(reviews_df['Text'][i], "\n\n")