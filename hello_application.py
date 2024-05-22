import tkinter as tk
from tkinter import messagebox
from classifiers import (
    classify_with_tfidf_naive_bayes, classify_with_bow_naive_bayes,
    classify_with_tfidf_logistic_regression, classify_with_bow_logistic_regression
)

class HelloApplication(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #centering Frame
        frame = tk.Frame(self)
        frame.grid(row=0, column=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        #email input label
        labelemail = tk.Label(frame, text="Email Input:", font=("Arial", 24))
        labelemail.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
        
        #email text space
        self.textemail = tk.Text(frame, height=15, font=("Arial", 16), wrap="word")
        self.textemail.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        self.textemail.insert(tk.END, "Write your email here..")
        self.textemail.bind("<FocusIn>", self.clear_placeholder)
        
        #check button
        checkbuton = tk.Button(frame, text="Check Input Email", bg="#6b6b6b", fg="white", font=("Arial", 16),
                                       width=20, height=2, command=self.on_check_input_email)
        checkbuton.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        #blackspace
        blackspace = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN)
        blackspace.grid(row=3, column=0, sticky="ew", padx=5, pady=20)

    def clear_placeholder(self, event):
        if self.textemail.get("1.0", tk.END).strip() == "Write your email here..":
            self.textemail.delete("1.0", tk.END)
            self.textemail.config(fg="black")

    def on_check_input_email(self):
        contentofemail = self.textemail.get("1.0", tk.END).strip()
        selectedvectormet = self.controller.selectedvectormet
        selectclassmet = self.controller.selectclassmet

        if selectedvectormet == "TF-IDF" and selectclassmet == "Naive Bayes":
            result = classify_with_tfidf_naive_bayes(contentofemail)
        elif selectedvectormet == "Bag of Words" and selectclassmet == "Naive Bayes":
            result = classify_with_bow_naive_bayes(contentofemail)
        elif selectedvectormet == "TF-IDF" and selectclassmet == "Logistic Regression":
            result = classify_with_tfidf_logistic_regression(contentofemail)
        elif selectedvectormet == "Bag of Words" and selectclassmet == "Logistic Regression":
            result = classify_with_bow_logistic_regression(contentofemail)

        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = HelloApplication(root, None)
    root.mainloop()
