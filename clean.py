import pandas as pd 
import re
import codecs
import itertools

from bs4 import BeautifulSoup

# Cleaning comments 
def cleaning(review):

    # Remove HTML tags using beautiful soup
    review = BeautifulSoup(review,"lxml").get_text()

    return review

# Read the csv file
reviews_df = pd.read_csv('Reviews.csv')

# Array to store comments
clean_reviews = []

# Loop through comments in 'Text' tag
for i in range(0, 20):

    # Clean text here 
    clean_review = cleaning(reviews_df['Text'][i])
    
    print(clean_review, "\n\n")