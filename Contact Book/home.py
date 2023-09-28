from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


class HomeWindow(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Home")
        self.state('zoomed')


if __name__ == "__main__":
    home = HomeWindow()
    home.mainloop()
