import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.introduction = tk.Button(self)
        self.introduction["text"] = "(Click here to start)"
        self.introduction["command"] = self.start_scene
        self.introduction.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def start_scene(self):
        print("Welcome to Math Blaster - A Space Terminal Adventure")


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# def resize(event):
#     print("New size is: {}x{}".format(event.width, event.height))


# root.bind("<Configure>", resize)
app = Application(master=root)
app.master.title("Math Cletson - A Mathematical Space Adventure")
app.mainloop()
