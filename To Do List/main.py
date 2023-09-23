import tkinter as tk
from datetime import date, datetime

Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

today = str(date.today())
dt = datetime.now()
day_no = dt.weekday()
month_no = int(today[5:7])

year = today[:4]
date = today[8:]
month = Months[month_no]
day = Days[day_no]

LARGEFONT = ("Arial", 20, "bold")
MIDFONT = ("Arial", 15, "bold")
SMALLFONT = ("Arial", 10, "bold")
GREENCOLOR = "#1b5d36"
LIGHTGREENCOLOR = "#2f8f56"
SELECTCOLOR = "#30734b"


class To_Do_List:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("To Do List")

        self.taskList = []
        self.scrollbar = None
        self.listbox = None
        self.frame1 = None
        self.frame = None
        self.task_entry = None
        self.task = None

        self.CreateIcons()
        self.Heading()
        self.ListBox()
        self.openTaskFile()
        self.createMain()
        self.createButton()

    def createMain(self):
        #     Main
        self.frame = tk.Frame(self.window, width=400, height=50, bg='white')
        self.frame.place(x=0, y=180)

        self.task = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, width=18, font=LARGEFONT, bd=0)
        self.task_entry.place(x=10, y=7)
        self.task_entry.focus()

    def createButton(self):
        #     Button
        self.Add = tk.Button(self.frame, text="ADD", font=LARGEFONT, width=6, bg=SELECTCOLOR, fg="#fff", bd=0,
                             command=self.addTask)
        self.Add.place(x=280, y=0)

        self.delete = tk.PhotoImage(file="Images/delete.png")
        tk.Button(self.window, image=self.delete, bd=0, command=self.deleteTask).pack(side=tk.BOTTOM, pady=10)

    def ListBox(self):
        #     ListBox
        self.frame1 = tk.Frame(self.window, bd=3, width=700, height=280, bg=LIGHTGREENCOLOR)
        self.frame1.pack(pady=(160, 0))

        self.listbox = tk.Listbox(self.frame1, font=MIDFONT, width=35, height=13, bg=LIGHTGREENCOLOR, fg="white",
                                  cursor="hand2", selectbackground=SELECTCOLOR)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
        self.scrollbar = tk.Scrollbar(self.frame1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def CreateIcons(self):
        # Icon
        Image_icon = tk.PhotoImage(file="Images/task.png")
        self.window.iconphoto(False, Image_icon)
        # Top Bar
        self.TopImage = tk.PhotoImage(file="Images/topbar.png")
        tk.Label(self.window, image=self.TopImage).pack()
        # Dock Image
        self.DockImage = tk.PhotoImage(file="Images/dock.png")
        tk.Label(self.window, image=self.DockImage, bg=GREENCOLOR).place(x=20, y=30)
        # Notebook Icon
        self.NoteImage = tk.PhotoImage(file="Images/task.png")
        tk.Label(self.window, image=self.NoteImage, bg=GREENCOLOR).place(x=320, y=25)

    def Heading(self):
        self.date = "{} {} {}".format(date, month, year)
        self.day = day
        self.text = "{} {}".format(self.day, self.date)
        self.heading = tk.Label(self.window, text="ALL TASK", font=LARGEFONT, fg="white", bg=GREENCOLOR)
        self.heading.place(x=110, y=15)
        self.DATE = tk.Label(self.window, text=self.text, font=SMALLFONT, fg="white", bg=GREENCOLOR)
        self.DATE.place(x=110, y=50)

    def addTask(self):
        task = self.task_entry.get()
        self.task_entry.delete(0, tk.END)

        if task:
            with open("Tasklist.txt", 'a') as taskfile:
                taskfile.write(f"\n{task}")
            self.taskList.append(task)
            self.listbox.insert(tk.END, task)

    def deleteTask(self):
        global taskList
        task = str(self.listbox.get(tk.ANCHOR))
        if task in self.taskList:
            self.taskList.remove(task)
            with open("Tasklist.txt", "w") as taskfile:
                for task in self.taskList:
                    taskfile.write(task + '\n')

            self.listbox.delete(tk.ANCHOR)

    def openTaskFile(self):
        try:
            global taskList
            with open("Tasklist.txt", "r") as taskfile:
                tasks = taskfile.readlines()

            for task in tasks:
                if task != '\n':
                    self.taskList.append(task)
                    self.listbox.insert(tk.END, task)

        except:
            file = open("Tasklist.txt", "w")
            file.close()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    to_do = To_Do_List()
    to_do.run()
