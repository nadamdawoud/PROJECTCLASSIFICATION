import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import os

class HelloApplication(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.method = None
        self.classifier = None

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        frame = tk.Frame(self)
        frame.grid(row=0, column=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        labelemail = tk.Label(frame, text="Email Input:", font=("Arial", 24))
        labelemail.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
        
        self.textemail = tk.Text(frame, height=15, font=("Arial", 16), wrap="word")
        self.textemail.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        self.textemail.insert(tk.END, "Write your email here..")
        
        checkbuton = tk.Button(frame, text="Check Input Email", bg="#6b6b6b", fg="white", font=("Arial", 16), width=20, height=2, command=self.on_check_input_email)
        checkbuton.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        blackspace = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN)
        blackspace.grid(row=3, column=0, sticky="ew", padx=5, pady=20)
    
    def set_method_and_classifier(self, method, classifier):
        self.method = method
        self.classifier = classifier
    
    def on_check_input_email(self):
        content = self.textemail.get("1.0", tk.END).strip()

        preprocess = pd.read_csv('preprocessed.csv')

        preprocess = preprocess.dropna(subset=['clean'])

        if self.method == "Bag of Words":
            vectorizer = CountVectorizer()
        else:
            vectorizer = TfidfVectorizer()

        X = vectorizer.fit_transform(preprocess['clean'])
        y = preprocess['label']

        if self.classifier == "Naive Bayes":
            classmodel = MultinomialNB()
        elif self.classifier == "SVM":
            classmodel = SVC()
        elif self.classifier == "Logistic Regression":
            classmodel = LogisticRegression()
        elif self.classifier == "Random Forest":
            classmodel = RandomForestClassifier()
        elif self.classifier == "KNN":
            classmodel = KNeighborsClassifier()

        classmodel.fit(X, y)

        vectorizedemail = vectorizer.transform([content])
        prediction = classmodel.predict(vectorizedemail)
        final = "Spam" if prediction[0] == 1 else "Not Spam"
        messagebox.showinfo("Email Classification Result", final)
