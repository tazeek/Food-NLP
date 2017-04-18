import pandas as pd 
import re
import codecs
import itertools
import nltk.data

from bs4 import BeautifulSoup

# Cleaning comments 
def cleaning(review):

    # Remove HTML tags using beautiful soup
    review = BeautifulSoup(review,"lxml").get_text()

    # Remove URLs
    review = re.sub(r'\w+:\/\/\S+', ' ', review)
 
    # Word Standardizing (Ex. Looooolll should be Looll)
    review = ''.join(''.join(s)[:2] for _, s in itertools.groupby(review))

    # Remove multiple occurrences of non-alphabets
    review = re.sub(r"(\W)\1+",r"\1", review)

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