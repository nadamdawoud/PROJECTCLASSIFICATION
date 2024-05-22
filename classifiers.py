# classifier.py
import pickle

#loading models and vectorizers
with open('models/tfidf_naive_bayes_model.pkl', 'rb') as file:
    tfidf_naive_bayes_model = pickle.load(file)

with open('models/tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

with open('models/bow_naive_bayes_model.pkl', 'rb') as file:
    bow_naive_bayes_model = pickle.load(file)

with open('models/bow_vectorizer.pkl', 'rb') as file:
    bow_vectorizer = pickle.load(file)

with open('models/tfidf_logistic_regression_model.pkl', 'rb') as file:
    tfidf_logistic_regression_model = pickle.load(file)

with open('models/bow_logistic_regression_model.pkl', 'rb') as file:
    bow_logistic_regression_model = pickle.load(file)

def classify_with_tfidf_naive_bayes(email_content):
    email_vector = tfidf_vectorizer.transform([email_content])
    prediction = tfidf_naive_bayes_model.predict(email_vector)
    return "Spam" if prediction == 1 else "Not Spam"

def classify_with_bow_naive_bayes(email_content):
    email_vector = bow_vectorizer.transform([email_content])
    prediction = bow_naive_bayes_model.predict(email_vector)
    return "Spam" if prediction == 1 else "Not Spam"

def classify_with_tfidf_logistic_regression(email_content):
    email_vector = tfidf_vectorizer.transform([email_content])
    prediction = tfidf_logistic_regression_model.predict(email_vector)
    return "Spam" if prediction == 1 else "Not Spam"

def classify_with_bow_logistic_regression(email_content):
    email_vector = bow_vectorizer.transform([email_content])
    prediction = bow_logistic_regression_model.predict(email_vector)
    return "Spam" if prediction == 1 else "Not Spam"
