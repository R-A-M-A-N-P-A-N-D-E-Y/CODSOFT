from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox


class LoginWindow(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Login")
        self.geometry("400x300")

        Icon = PhotoImage(file="Images/user.png")
        self.iconphoto(False, Icon)

        s = Style()
        s.configure('Header.TFrame', background='blue')

        header_frame = Frame(self, style='Header.TFrame')
        header_frame.pack(fill=X)

        s.configure('Header.TLabel', background='blue', foreground='white', font=('Arial', 25))

        header_label = Label(header_frame, text="My Contact Book", style='Header.TLabel')
        header_label.pack(pady=10)

        s.configure('Content.TFrame', background='white')

        content_frame = Frame(self, style='Content.TFrame')
        content_frame.pack(fill=BOTH, expand=True)

        login_frame = Frame(content_frame, style='Content.TFrame')
        login_frame.place(relx=.5, rely=.5, anchor=CENTER)

        img = (Image.open("Images/user1.png"))
        resized_image = img.resize((55, 50))
        content_frame.user = ImageTk.PhotoImage(resized_image)
        login_user = Label(login_frame, image=content_frame.user, background='white', foreground='white')
        login_user.image = content_frame.user
        login_user.grid(row=0, column=1)

        login_label = Label(login_frame, text='Login', background='white', font=('Arial', 20))
        login_label.grid(row=1, column=1)

        img = (Image.open("Images/user.png"))
        resized_image = img.resize((25, 25))
        content_frame.user = ImageTk.PhotoImage(resized_image)
        username_label = Label(login_frame, image=content_frame.user, background='white', foreground='white')
        username_label.grid(row=2, column=0)

        username_entry = Entry(login_frame)
        username_entry.grid(row=2, column=1, pady=5)

        img = (Image.open("Images/lock.png"))
        resized_image = img.resize((25, 25))
        content_frame.lock = ImageTk.PhotoImage(resized_image)
        password_label = Label(login_frame, image=content_frame.lock, background='white', foreground='white')
        password_label.grid(row=3, column=0)

        password_entry = Entry(login_frame)
        password_entry.grid(row=3, column=1, pady=5)

        login_button = Button(login_frame, text="Login")
        login_button.grid(row=4, column=1, pady=5)


if __name__ == "__main__":
    login = LoginWindow()
    login.mainloop()
