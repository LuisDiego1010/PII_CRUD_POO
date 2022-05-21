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

    def Read_menu(self):
        self = Window()
        self.title("Read Menu")
        file_read_students=PhotoImage(file="resourses//images//btn_read_students.png",master=self)
        btn_read_students = Button(image=file_read_students,width=150,height=150,master=self)
        btn_read_students.place(x=315, y=220)
        file_read_student=PhotoImage(file="resourses//images//btn_read_student.png",master=self)
        btn_read_student = Button(image=file_read_student,width=150,height=150,master=self)
        btn_read_student.place(x=515, y=220)
        file_read_courses=PhotoImage(file="resourses//images//btn_read_courses.png",master=self)
        btn_read_courses = Button(image=file_read_courses,width=150,height=150,master=self)
        btn_read_courses.place(x=715, y=220)
        self.mainloop()

    def Update_menu(self):
        self = Window()
        self.title("Update Menu")
        file_update_information=PhotoImage(file="resourses//images//btn_information.png",master=self)
        btn_update_information= Button(image=file_update_information,width=150,height=150,master=self)
        btn_update_information.place(x=430, y=220)
        file_update_calification=PhotoImage(file="resourses//images//btn_calification.png",master=self)
        btn_update_calification = Button(image=file_update_calification,width=150,height=150,master=self)
        btn_update_calification.place(x=650, y=220)
        self.mainloop()

    def Delete_menu(self):
        self = Window()
        self.title("Delete Menu")
        file_delete_student=PhotoImage(file="resourses//images//btn_delete_student.png",master=self)
        btn__new_student = Button(image=file_delete_student,width=150,height=150,master=self)
        btn__new_student.place(x=430, y=220)
        file_delete_course=PhotoImage(file="resourses//images//btn_delete_course.png",master=self)
        btn_delete_course = Button(image=file_delete_course,width=150,height=150,master=self)
        btn_delete_course.place(x=650, y=220)
        self.mainloop()

    def Principal_Menu(self):
        #Create button
        self.file_create=PhotoImage(file="resourses//images//btn_create.png",master=self)
        self.btn_create = Button(image=self.file_create,width=150,height=150,command=self.Create_menu)
        self.btn_create.place(x=360, y=220)
        #Read button
        self.file_read=PhotoImage(file="resourses//images//btn_read.png")
        self.btn_read = Button(image=self.file_read,width=150,height=150,command=self.Read_menu)
        self.btn_read.place(x=690, y=220)
        #Update button    
        self.file_update=PhotoImage(file="resourses//images//btn_update.png")
        self.btn_update = Button(image=self.file_update,width=150,height=150,command=self.Update_menu)
        self.btn_update.place(x=360, y=420)
        #Delete button
        self.file_delete=PhotoImage(file="resourses//images//btn_delete.png")
        self.btn_delete = Button(image=self.file_delete,width=150,height=150,command=self.Delete_menu)
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
