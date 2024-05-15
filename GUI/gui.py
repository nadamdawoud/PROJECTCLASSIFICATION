import tkinter as tk
from starting_page import StartingPage
from hello_application import HelloApplication


import pickle

with open('models.pkl', 'rb') as f:
    models = pickle.load(f)

    print(models)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application")
        self.geometry("400x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartingPage, HelloApplication):
            page = F.__name__
            frame = F(framebef=self, controller=self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_start_menu("StartingPage")

    def show_start_menu(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def show_main_menu(self, page, technique, classifier):
        frame = self.frames[page]
        frame.tkraise()
        
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
