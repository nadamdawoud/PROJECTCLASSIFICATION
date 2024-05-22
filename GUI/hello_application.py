import tkinter as tk
from tkinter import messagebox

class HelloApplication(tk.Frame):
    def __init__(self, framebef, controller):
        super().__init__(framebef)
        self.controller = controller

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # centering frame
        framecent = tk.Frame(self)
        framecent.grid(row=0, column=0)
        framecent.grid_columnconfigure(0, weight=1)
        framecent.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        # email input
        labelemail = tk.Label(framecent, text="Email Input:", font=("Arial", 24))
        labelemail.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
        
        # email text space
        self.textemail = tk.Text(framecent, height=15, font=("Arial", 16), wrap="word")
        self.textemail.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        self.textemail.insert(tk.END, "Write your email here..")
        self.textemail.bind("<FocusIn>", self.clearholder)
        
        # check input button
        checkbuton = tk.Button(framecent, text="Check Input Email", bg="#6b6b6b", fg="white", font=("Arial", 16),
                               width=20, height=2, command=self.checkinputemailclick)
        checkbuton.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
        
        # separator
        blackspace = tk.Frame(framecent, height=2, bd=1, relief=tk.SUNKEN)
        blackspace.grid(row=3, column=0, sticky="ew", padx=5, pady=20)
        
        # ham Button
        hambutton = tk.Button(framecent, text="Ham", bg="#8BC34A", fg="white", font=("Arial", 16), width=20, height=2, command=self.hambuttonclick)
        hambutton.grid(row=4, column=0, pady=10, padx=20, sticky="ew")
        
        # spam Button
        spambutton = tk.Button(framecent, text="Spam", bg="#F44336", fg="white", font=("Arial", 16), width=20, height=2, command=self.spambuttonclick)
        spambutton.grid(row=5, column=0, pady=10, padx=20, sticky="ew")
        
    #to clear the text when user clicks
    def clearholder(self, event):
        if self.textemail.get("1.0", tk.END).strip() == "Write your email here..":
            self.textemail.delete("1.0", tk.END)

    def checkinputemailclick(self):
        contentofemail = self.textemail.get("1.0", tk.END).strip()
        print("clicked")    

    def hambuttonclick(self):
        print("clicked")     

    def spambuttonclick(self):
        print("clicked")  
