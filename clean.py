import pandas as pd 
import re
import codecs
import itertools
import nltk.data

from contractions import contractions
from bs4 import BeautifulSoup

# Load tokenizer 
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Cleaning comments 
def cleaningComment(review):

    # Remove HTML tags using beautiful soup
    review = BeautifulSoup(review,"lxml").get_text()

    # Remove Unicode characters
    review = codecs.decode(review, 'unicode-escape')
    review = ''.join([i if ord(i) < 128 else '' for i in review])

    # Remove URLs
    review = re.sub(r'\w+:\/\/\S+', ' ', review)
 
    # Word Standardizing (Ex. Looooolll should be Looll)
    review = ''.join(''.join(s)[:2] for _, s in itertools.groupby(review))

    # Remove multiple occurrences of non-alphabets
    review = re.sub(r"(\W)\1+",r"\1", review)

    # Convert words to lower case and split them
    words = review.lower().split()

    # Remove contractions by expansion of words
    words = [contractions[word] if word in contractions else word for word in words]

    # Rejoin words 
    review = " ".join(words)

    return review

# Cleaning sentences 
def cleaningSentence(sentence):

    # Remove non-alphanumeric characters

    # Convert words to lower case and split them 

    # Remove contractions by expansion of words 

    # Rejoin words

# Tokenize Sentences
def tokenize(review):

    # Tokenize sentence here 
    sentences = tokenizer.tokenize(review)
    clean_sentence = []

    print(sentences)
    
    return sentences

# Read the csv file
reviews_df = pd.read_csv('Reviews.csv')

# Array to store comments and sentences
clean_reviews = []
sentences = []

# Loop through comments in 'Text' tag
for i in range(0, 20):

    # Clean text here 
    clean_review = cleaning(reviews_df['Text'][i])

    clean_reviews.append(clean_review)

# Loop through each review 
for i in range(0,20):

    # Sentence Segmentation
    clean_sentences = tokenize(clean_reviews[i])

    #for sentence in clean_sentences:
        #print(sentence)

    print("\n\n")