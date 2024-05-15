import tkinter as tk
from tkinter import ttk

class StartingPage(tk.Frame):
    def __init__(self, framebef, controller):
        super().__init__(framebef)
        self.controller = controller

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        framecent = tk.Frame(self)
        framecent.grid(row=0, column=0)
        framecent.grid_columnconfigure(0, weight=1)
        framecent.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)

        # dropdown for tfidf-bagofwords
        self.label1 = tk.Label(framecent, text="Choose Method:", font=("Arial", 16))
        self.label1.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
        
        self.method = tk.StringVar()
        self.dropdown = ttk.Combobox(framecent, textvariable=self.method, values=["Bag of Words", "TF-IDF"], font=("Arial", 16), state="readonly")
        self.dropdown.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        self.dropdown.set("Bag of Words")
        
        # dropdown for methods 
        # NOTE : CHANGE THE NAMES OF BUTTONS
        self.label2 = tk.Label(framecent, text="Choose Option:", font=("Arial", 16),)
        self.label2.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        self.option = tk.StringVar()
        self.dropdown = ttk.Combobox(framecent, textvariable=self.option, values=["1", "2", "3", "4", "5"], font=("Arial", 16), state="readonly")
        self.dropdown.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
        self.dropdown.set("1")
        
        # continue button
        self.continuebutton = tk.Button(framecent, text="Continue", font=("Arial", 16), command=self.on_continue)
        self.continuebutton .grid(row=4, column=0, pady=20, padx=20, sticky="ew")

    def on_continue(self):
        self.controller.show_frame("HelloApplication")
