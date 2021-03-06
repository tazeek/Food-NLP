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

    # Remove encodings
    review = re.sub(r'\\\\', r'\\', review)
    review = re.sub(r'\\', ' ', review)
    review = re.sub(r'\\x\w{2,2}', ' ', review)
    review = re.sub(r'\\u\w{4,4}', ' ', review)
    review = re.sub(r'\\n', '.', review)

    # Remove Unicode characters
    try:
        review = codecs.decode(review, 'unicode-escape')
        review = ''.join([i if ord(i) < 128 else '' for i in review])
    except UnicodeDecodeError:
        print(review)
        exit()

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
total_reviews = len(reviews_df)

# Array to store comments and sentences
clean_reviews = []
sentences = []

# Loop through comments in 'Text' tag
print("\n", "=" * 30)
print("CLEAING REVIEWS")
print("=" * 30, "\n")

for i, review in enumerate(reviews_df['Text']): 

    # Clean text here 
    clean_review = cleaningComment(reviews_df['Text'][i])

    clean_reviews.append(clean_review)

    if i % 10000 == 0:
        print("%d out of %d  reviews cleaned" % (i, total_reviews))

# Loop through each review 
print("=" * 30)
print("\n\nSENTENCE SEGMENTATION")
print("=" * 30, "\n")

for i, review in enumerate(clean_reviews):

    # Sentence Segmentation
    clean_sentences = tokenizeSentence(review)

    # Append sentences 
    for sentence in clean_sentences:
        sentences.append(sentence)

    if i % 10000 == 0:
        print("%d out of %d  reviews segmented" % (i, total_reviews))

# Convert to data frame 
df = pd.DataFrame(data={'sentence': sentences})

# Save the dataframe in CSV format 
df.to_csv('clean_sentences.csv', index=False)