from tkinter import *
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        #Window Variables
        super(Window,self).__init__()
        self.geometry("1200x700")
        self.file=PhotoImage(file="resourses//images//menu_2.png",master=self)
        self.background=Label(self, image=self.file)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)

    def Create_menu(self):
        self = Window()
        self.title("Create Menu")
        file_new_student=PhotoImage(file="resourses//images//btn_new_student.png",master=self)
        btn__new_student = Button(image=file_new_student,width=150,height=150,master=self)
        btn__new_student.place(x=430, y=220)
        file_new_course=PhotoImage(file="resourses//images//btn_new_course.png",master=self)
        btn__new_course = Button(image=file_new_course,width=150,height=150,master=self)
        btn__new_course.place(x=650, y=220)

        
        self.mainloop()

    def Principal_Menu(self):
        #Create button
        self.file_create=PhotoImage(file="resourses//images//btn_create.png",master=self)
        self.btn_create = Button(image=self.file_create,width=150,height=150,command=self.Create_menu)
        self.btn_create.place(x=360, y=220)
        #Read button
        self.file_read=PhotoImage(file="resourses//images//btn_read.png")
        self.btn_read = Button(image=self.file_read,width=150,height=150)
        self.btn_read.place(x=690, y=220)
        #Update button    
        self.file_update=PhotoImage(file="resourses//images//btn_update.png")
        self.btn_update = Button(image=self.file_update,width=150,height=150)
        self.btn_update.place(x=360, y=420)
        #Delete button
        self.file_delete=PhotoImage(file="resourses//images//btn_delete.png")
        self.btn_delete = Button(image=self.file_delete,width=150,height=150)
        self.btn_delete.place(x=690, y=420)
        #Exit button
        self.file_exit=PhotoImage(file="resourses//images//btn_exit.png")
        self.btn_exit = Button(image=self.file_exit,width=150,height=150,command=self.quit)
        self.btn_exit.place(x=1000, y=530)
        self.mainloop()
    


#WINDOWS
def main_window():
    app = Window()
    app.title("Menu")
    app.file=PhotoImage(file="resourses//images//menu.png")
    app.background=Label(app, image=app.file)
    app.background.place(x=0,y=0,relwidth=1,relheight=1)
    app.Principal_Menu()
    app.mainloop()

main_window()
