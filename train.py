import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import os

#load the data
preprocessed = pd.read_csv('preprocessed.csv')

#handle missing values
preprocessed['clean'].fillna('', inplace=True)

X = preprocessed['clean']
y = preprocessed['label']

#splitting the data
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

#create directory if doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

#tf-idf vectorizer
tfidfvector = TfidfVectorizer()
xtraintfidf = tfidfvector.fit_transform(xtrain)

#train naive bayes 
tfidfnaivebayes = MultinomialNB()
tfidfnaivebayes.fit(xtraintfidf, ytrain)

#train logistic regression 
tfidflogisticreg = LogisticRegression(max_iter=1000)
tfidflogisticreg.fit(xtraintfidf, ytrain)

#save
with open('models/tfidf_vectorizer.pkl', 'wb') as file:
    pickle.dump(tfidfvector, file)

with open('models/tfidf_naive_bayes_model.pkl', 'wb') as file:
    pickle.dump(tfidfnaivebayes, file)

with open('models/tfidf_logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(tfidflogisticreg, file)

#bog vectorizer
bowvector = CountVectorizer()
xtrainbow = bowvector.fit_transform(xtrain)

#train naive bayes
bownaive = MultinomialNB()
bownaive.fit(xtrainbow, ytrain)

#train logistic regression 
bowlogistreg = LogisticRegression(max_iter=1000)
bowlogistreg.fit(xtrainbow, ytrain)

#save   
with open('models/bow_vectorizer.pkl', 'wb') as file:
    pickle.dump(bowvector, file)

with open('models/bow_naive_bayes_model.pkl', 'wb') as file:
    pickle.dump(bownaive, file)

with open('models/bow_logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(bowlogistreg, file)

print("Models and vectorizers have been saved successfully.")
