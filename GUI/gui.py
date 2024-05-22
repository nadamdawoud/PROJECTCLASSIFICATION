import tkinter as tk
from starting_page import StartingPage
from hello_application import HelloApplication

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
            frame = F(parent=self, controller=self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartingPage")

    def show_frame(self, page_name, method=None, classifier=None):
        frame = self.frames[page_name]
        if page_name == "HelloApplication":
            frame.set_method_and_classifier(method, classifier)
        frame.tkraise()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
