import pandas as pd 
import re
import codecs
import itertools

from nltk.tokenize import sent_tokenize
from contractions import contractions
from bs4 import BeautifulSoup

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
    sentence = re.sub("[^a-zA-Z0-9'\s]", " ", sentence)

    # Convert words to lower case  
    sentence = sentence.lower().split()

    # Remove contractions by expansion of words
    words = [contractions[word] if word in contractions else word for word in sentence]

    # Rejoin words
    sentence = " ".join(words)

    return sentence 

# Tokenize Sentences
def tokenizeSentence(review):

    # Tokenize sentence here 
    sentences = sent_tokenize(review)
    clean_sentences = []

    for sentence in sentences:
        
        # Clean sentence here 
        clean_sentence = cleaningSentence(sentence)
        clean_sentences.append(clean_sentence)
    
    return clean_sentences

# Read the csv file
reviews_df = pd.read_csv('Reviews.csv')

# Array to store comments and sentences
clean_reviews = []
sentences = []

# Loop through comments in 'Text' tag
for i in range(0, 10):

    # Clean text here 
    clean_review = cleaningComment(reviews_df['Text'][i])

    clean_reviews.append(clean_review)

# Loop through each review 
for i in range(0,10):

    # Sentence Segmentation
    clean_sentences = tokenizeSentence(clean_reviews[i])

    # Append sentences 
    for sentence in clean_sentences:
        sentences.append(sentence)


# Convert to data frame 
df = pd.DataFrame(data={'sentence': sentences})

# Save the dataframe in CSV format 
df.to_csv('clean_sentences.csv', index=False)