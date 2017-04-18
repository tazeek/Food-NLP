import pandas as pd 
import numpy as np 
import re
import codecs
import time
import os
import itertools


# Read the csv file
reviews_df = pd.read_csv('Reviews.csv')

print(len(reviews_df))