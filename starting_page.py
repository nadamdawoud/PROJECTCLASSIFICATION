# starting_page.py
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
        frame.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)

        #dropdown menu1
        self.label1 = tk.Label(frame, text="Choose Vectorization Method:", font=("Arial", 16))
        self.label1.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
        
        self.vectmethodvar = tk.StringVar()
        self.vectmethoddrop = ttk.Combobox(
            frame, textvariable=self.vectmethodvar, 
            values=["Bag of Words", "TF-IDF"], 
            font=("Arial", 16),
            state='readonly'
        )
        self.vectmethoddrop.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        self.vectmethoddrop.set("Bag of Words")
        
        #dropdown menu2
        self.label2 = tk.Label(frame, text="Choose Classification Method:", font=("Arial", 16))
        self.label2.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        self.classmethodvar = tk.StringVar()
        self.classmetdrop = ttk.Combobox(
            frame, textvariable=self.classmethodvar, 
            values=["Naive Bayes", "Logistic Regression"], 
            font=("Arial", 16),
            state='readonly'
        )
        self.classmetdrop.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
        self.classmetdrop.set("Naive Bayes")
        
        #continue button
        self.continuebutton = tk.Button(frame, text="Continue", font=("Arial", 16), command=self.on_continue)
        self.continuebutton.grid(row=4, column=0, pady=20, padx=20, sticky="ew")

    def on_continue(self):
        selectedvectormet = self.vectmethodvar.get()
        selectclassmet = self.classmethodvar.get()
        self.controller.selectedvectormet = selectedvectormet
        self.controller.selectclassmet = selectclassmet
        self.controller.show_frame("HelloApplication")
