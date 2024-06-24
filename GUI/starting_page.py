import tkinter as tk
from tkinter import ttk

class StartingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        frame = tk.Frame(self)
        frame.grid(row=0, column=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)

        # Dropdown for Bag of Words or TF-IDF
        self.label1 = tk.Label(frame, text="Choose Method:", font=("Arial", 16))
        self.label1.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
        
        self.varmethod = tk.StringVar()
        self.drop1 = ttk.Combobox(frame, textvariable=self.varmethod, values=["Bag of Words", "TF-IDF"], font=("Arial", 16), state='readonly')
        self.drop1.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        self.drop1.set("Choose")
        
        # Dropdown for options 1-5
        self.label2 = tk.Label(frame, text="Choose Option:", font=("Arial", 16))
        self.label2.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        self.classvar = tk.StringVar()
        self.dropdown2 = ttk.Combobox(frame, textvariable=self.classvar, values=["Logistic Regression", "Naive Bayes", "Support Vector Machine"], font=("Arial", 16), state='readonly')
        self.dropdown2.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
        self.dropdown2.set("Choose")
        
        # Continue button
        self.contbutton = tk.Button(frame, text="Continue", font=("Arial", 16), command=self.on_continue)
        self.contbutton.grid(row=4, column=0, pady=20, padx=20, sticky="ew")

    def on_continue(self):
        # Store selections in controller
        self.controller.method = self.varmethod.get()
        self.controller.classifier = self.classvar.get()
        self.controller.show_frame("HelloApplication")
