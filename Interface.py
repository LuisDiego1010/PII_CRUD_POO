from tkinter import *
from turtle import back

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)
        #self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.handler
        self.hi_there.pack(side="top",padx=10, pady=10)
        self.hi_there.config(bg='blue', fg='white',font=('times',10,'bold italic'))
        self.hi_there.config(bd=10,relief=RAISED)
        self.quit = Button(self, text="Finish",command=self.master.destroy)
        self.quit.pack(side="bottom",fill=X, expand=YES)
        self.quit.config(bd=10, relief=RAISED)
        self.quit.config(bg='black',fg='yellow',font=('times',30,'bold normal'))

    def handler(self):
        print("Hola todos!")

#FUNCIONES DE VENTANAS
def main_window():
    root = Tk()
    root.geometry("1200x700")
    app = Application(master=root)
    c=Canvas(app,bg="gray16",height=200,width=200)
    file_menu=PhotoImage(file="resourses//images//menu.png")
    background=Label(app, image=file_menu)
    background.place(x=0,y=0,relwidth=1,relheight=1)

    app.master.title("Menu Window")
    c.pack()
    app.mainloop()

main_window()

def window_create():
    root = Tk()
    root.geometry("1200x700")
    app = Application(master=root)
    c=Canvas(app,bg="gray16",height=200,width=200)
    file_menu=PhotoImage(file="resourses//images//menu_2.png")
    background=Label(app, image=file_menu)
    background.place(x=0,y=0,relwidth=1,relheight=1)

    app.master.title("Menu Window")
    c.pack()
    app.mainloop()


