from tkinter import *
import tkinter as tk
import shelve
archive = "students_base"

class Student():
    carnet=0
    name=""
    direction=""
    telephone=0
    email=""
    cursos={}


class App(tk.Tk):
    #Constructor of class App
    def __init__(self):
        #Atributes of class App
        super(App,self).__init__()
        self.geometry("1200x700")
        self.file=PhotoImage(file="resourses//images//menu_2.png",master=self)
        self.background=Label(self, image=self.file)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)
        
    #Methods of class App
    def Create_menu(self):
        self = App()
        self.title("Create Menu")
        file_new_student=PhotoImage(file="resourses//images//btn_new_student.png",master=self)
        btn__new_student = Button(image=file_new_student,width=150,height=150,master=self,command=self.Create_student_app)
        btn__new_student.place(x=430, y=220)
        file_new_course=PhotoImage(file="resourses//images//btn_new_course.png",master=self)
        btn__new_course = Button(image=file_new_course,width=150,height=150,master=self,command=self.Create_course_app)
        btn__new_course.place(x=650, y=220)
        self.mainloop()

    def Read_menu(self):
        self = App()
        self.title("Read Menu")
        file_read_students=PhotoImage(file="resourses//images//btn_read_students.png",master=self)
        btn_read_students = Button(image=file_read_students,width=150,height=150,master=self,command=self.Read_studens_app)
        btn_read_students.place(x=315, y=220)
        file_read_student=PhotoImage(file="resourses//images//btn_read_student.png",master=self)
        btn_read_student = Button(image=file_read_student,width=150,height=150,master=self)
        btn_read_student.place(x=515, y=220)
        file_read_courses=PhotoImage(file="resourses//images//btn_read_courses.png",master=self)
        btn_read_courses = Button(image=file_read_courses,width=150,height=150,master=self)
        btn_read_courses.place(x=715, y=220)
        self.mainloop()

    def Update_menu(self):
        self = App()
        self.title("Update Menu")
        file_update_information=PhotoImage(file="resourses//images//btn_information.png",master=self)
        btn_update_information= Button(image=file_update_information,width=150,height=150,master=self)
        btn_update_information.place(x=430, y=220)
        file_update_calification=PhotoImage(file="resourses//images//btn_calification.png",master=self)
        btn_update_calification = Button(image=file_update_calification,width=150,height=150,master=self)
        btn_update_calification.place(x=650, y=220)
        self.mainloop()

    def Delete_menu(self):
        self = App()
        self.title("Delete Menu")
        file_delete_student=PhotoImage(file="resourses//images//btn_delete_student.png",master=self)
        btn__new_student = Button(image=file_delete_student,width=150,height=150,master=self)
        btn__new_student.place(x=430, y=220)
        file_delete_course=PhotoImage(file="resourses//images//btn_delete_course.png",master=self)
        btn_delete_course = Button(image=file_delete_course,width=150,height=150,master=self)
        btn_delete_course.place(x=650, y=220)
        self.mainloop()
    
    def Create_student_app(self):
        self=App()
        self.title("App Create Student")
        title = Label (self,text="Favor llene los espacios con la información solicitada:", font=("Adobe Gothic Std B",24),background="white").place(x=200,y=15)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=370,y=75)
        lbl_course = Label (self,text="Digite el curso que desea agregar al estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=135)
        ent_course= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=535,y=135)
        lbl_name = Label (self,text="Digite el nombre del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=195)
        ent_name= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=384,y=195)
        lbl_direction = Label (self,text="Digite la dirección del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=255)
        ent_direction= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=399,y=255)
        lbl_telephone = Label (self,text="Digite el telefono del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=315)
        ent_telephone= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=390,y=315)
        lbl_email = Label (self,text="Digite el email del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=375)
        ent_email= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=364,y=375)
        self.mainloop()

    def Create_course_app(self):
        self=App()
        self.title("App Create Course")
        title = Label (self,text="Favor llene los espacios con la información solicitada:", font=("Adobe Gothic Std B",24),background="white").place(x=200,y=15)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=370,y=75)
        lbl_course = Label (self,text="Digite el curso que desea agregar al estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=135)
        ent_course= Entry(self,font=("Adobe Gothic Std B",16),width=35).place(x=535,y=135)

    def Read_studens_app(self):
        self=App()
        # Create the text widget
        text_widget = tk.Text(self, height=5, width=40)
        # Create a scrollbar
        scroll_bar = tk.Scrollbar(self)
        # Pack the scroll bar
        # Place it to the right side, using tk.RIGHT
        scroll_bar.pack(side=tk.RIGHT)
        # Pack it into our tkinter application
        # Place the text widget to the left side
        text_widget.pack(side=tk.LEFT)
        long_text = """This is a multiline string.
        We can write this in multiple lines too!
        Hello from AskPython. This is the third line.
        This is the fourth line. Although the length of the text is longer than
        the width, we can use tkinter's scrollbar to solve this problem!
        """
        # Insert text into the text widget
        text_widget.insert(tk.END, long_text)
        # Start the mainloop
        mainloop()

        


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
    
#AppS
def main_App():
    app = App()
    app.title("Menu")
    app.file=PhotoImage(file="resourses//images//menu.png")
    app.background=Label(app, image=app.file)
    app.background.place(x=0,y=0,relwidth=1,relheight=1)
    app.Principal_Menu()
    app.mainloop()

main_App()