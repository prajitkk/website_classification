# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
# Importing the dataset
dataset = pd.read_csv('eggs.tsv', delimiter = '\t', quoting = 0,header = None)
#print (dataset[0][0])
# Cleaning the texts
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 9):
    review = re.sub('[^a-zA-Z]', ' ', dataset[0][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1000)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X, y)

website = input("enter a website")
r  = requests.get(website)
data = r.text
my_data =""
soup = BeautifulSoup(data, 'lxml')
for link in soup.find_all('p'):
    #print(link.text)
    my_data = my_data + link.text
    my_data = my_data
# Predicting the Test set results
my_corpus = []
my_test = re.sub('[^a-zA-Z]', ' ', my_data)
my_test = my_test.lower()
my_test = my_test.split()
my_test = [ps.stem(word) for word in my_test if not word in set(stopwords.words('english'))]
my_test = ' '.join(my_test)
corpus.append(my_test)

my_check = cv.fit_transform(corpus).toarray()
y_pred = classifier.predict(my_check[len(my_check)-1])
if(y_pred == 0):
    print("not technological")
else:
    print("technological")

# Making the Confusion Matrix
#from sklearn.metrics import confusion_matrix
#cm = confusion_matrix(y_test, y_pred)