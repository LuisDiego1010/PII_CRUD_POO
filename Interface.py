from tkinter import *
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        #Window Variables
        super(Window,self).__init__()
        self.geometry("1200x700")
        self.file=PhotoImage(file="resourses//images//menu_2.png")
        self.background=Label(self, image=self.file)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)
        
        #self.create_widgets()

#FUNCIONES DE VENTANAS
def main_window():
    app = Window()
    app.title("Menu")
    app.file=PhotoImage(file="resourses//images//menu.png")
    app.background=Label(app, image=app.file)
    app.background.place(x=0,y=0,relwidth=1,relheight=1)
    app.mainloop()

main_window()

def window_create():
    app = Window()
    app.title("Create Menu")

    app.mainloop()

window_create()

def window_read():
    app = Window()
    app.title("Read Menu")
    app.mainloop()
#window_read()

def window_update():
    app = Window()
    app.title("Update Menu")
    app.mainloop()

#window_update()

def window_delete():
    app = Window()
    app.title("Delete Menu")
    app.mainloop()

#window_delete()

