import re
from tkinter import *
import tkinter as tk
import shelve
from tkinter import messagebox

#Clase para almacenar toda la información de cada estudiante
class Student():
    def __init__(self)->None:
        self.carnet=0    
        self.course={}
        self.name=""
        self.direction=""
        self.telephone=0
        self.email=""


    def set_carnet(self,carnet):
        self.carnet=carnet
    
    def get_carnet(self):
        return self.carnet
        
    def set_course(self,course):
        self.course={course:0}
    
    def get_course(self):
        return self.course

    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        return self.name

    def set_direction(self,direction):
        self.direction=direction
    
    def get_direction(self):
        return self.direction
        
    def set_telephone(self,telephone):
        self.telephone=telephone
    
    def get_telephone(self):
        return self.telephone

    def set_email(self,email):
        self.email=email
    
    def get_email(self):
        return self.email

    def get_information(self):
        return [self.carnet,self.name,self.course,self.direction,self.telephone,self.email] 

class Data_Base():
    def __init__(self)->None:
        self.archive = "students_base"

    def busy(self):
        with shelve.open(self.archive, writeback=True) as students:
            if len(students)>0:
                return True
            else: 
                return False
    
    def found_carnet(self,carnet):
        with shelve.open(self.archive, writeback=True) as students:
            if str(carnet) in students:
                return True
            else: 
                return False
    
    def found_course(self,carnet,course):
        with shelve.open(self.archive, writeback=True) as students:
            if str(course) in (students[str(carnet)]["Cursos"]):
                return True
            else:
                False
            
    def add_course(self,carnet,course):
        with shelve.open(self.archive, writeback=True) as students:
            course_temp=students[carnet]["Cursos"][course]=0
            print(course_temp)

    def set_information(self,students_list):
        with shelve.open(self.archive, writeback=True) as students:
            carnet=students_list[0]
            name=students_list[1]
            courses=students_list[2]
            direction=students_list[3]
            telephone=students_list[4]
            email=students_list[5]
            students[carnet]= {"Nombre":name,"Cursos":courses,"Direccion":direction,"Telefono":telephone,"Email":email}
            print(students)
        students.close()
    
    def get_students(self):
        text = ""
        with shelve.open(self.archive, writeback=True) as students:
            if self.busy()==True:
                for i,j in students.items():
                    text += "\n\nEstudiante = " + i +":"
                    for f,z in j.items():
                        text += "\n" + str(f) + ":" + str(z) 
        students.close()
        return text
    
    def get_student(self,carnet):
        with shelve.open(self.archive, writeback=True) as students:
            text=""
            for i,j in students.items():
                if i == str(carnet):
                    text+="La información del estudiante con carnet "+ i + " es: \n"
                    for f,z in j.items():
                        text += str(f) + ":" + str(z) + "\n"
        students.close()
        return text

    def get_courses(self,carnet):
        with shelve.open(self.archive, writeback=True) as students:
            characters="{}"
            text=" "
            for i,j in students.items():
                if i == str(carnet):
                    print("Los cursos de",i, "son: ")
                    conversion=str(j["Cursos"])
                    for x in range(len(characters)):
                        conversion = conversion.replace(characters[x],"")
                    text += "Los cursos de " + i + " son: \n"+conversion.replace(",","\n")
        students.close()
        return text            
    
    def change_information(self,carnet,name,direction,telephone,email):
        with shelve.open(self.archive, writeback=True) as students:
            if len(name)!=0:
                print("ACTUALIZADO EL NOMBRE")
                for i,j in students.items():
                    if i == str(carnet):
                        j["Nombre"]=name
                        print("ACTUALIZADO EL NOMBRE")

            if len(direction)!=0:
                for i,j in students.items():
                    if i == str(carnet):
                        j["Direccion"]=direction

            if len(telephone)!=0:
                for i,j in students.items():
                    if i == str(carnet):
                        j["Telefono"]=telephone

            if len(email)!=0:
                for i,j in students.items():
                    if i == str(carnet):
                        j["Email"]=email

    def set_calification(self,carnet,course,new_calification):    
        with shelve.open(self.archive, writeback=True) as students:
            if str(course) in (students[str(carnet)]["Cursos"]):
                for i,j in students.items():
                    for k,l in j["Cursos"].items():
                        if i==str(carnet) and k == str(course):
                            j["Cursos"][k] = new_calification
        
    def delete_student(self, carnet):
        with shelve.open(self.archive, writeback=True) as students:
            del students[str(carnet)]
        
    def delete_course(self, carnet,course):
        with shelve.open(self.archive, writeback=True) as students:
            del (students[str(carnet)]["Cursos"][course])

class App(tk.Tk):
    #Constructor of class App
    def __init__(self):
        #Atributes of class App
        super(App,self).__init__()
        self.geometry("1200x700")
        self.file=PhotoImage(file="resourses//images//menu_2.png",master=self)
        self.background=Label(self, image=self.file)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)
        self.student=Student()
        self.db=Data_Base()
        
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
        btn_read_student = Button(image=file_read_student,width=150,height=150,master=self,command=self.Read_student_app)
        btn_read_student.place(x=515, y=220)
        file_read_courses=PhotoImage(file="resourses//images//btn_read_courses.png",master=self)
        btn_read_courses = Button(image=file_read_courses,width=150,height=150,master=self,command=self.Read_courses_app)
        btn_read_courses.place(x=715, y=220)
        self.mainloop()

    def Update_menu(self):
        self = App()
        self.title("Update Menu")
        file_update_information=PhotoImage(file="resourses//images//btn_information.png",master=self)
        btn_update_information= Button(image=file_update_information,width=150,height=150,master=self,command=self.Update_information_app)
        btn_update_information.place(x=430, y=220)
        file_update_calification=PhotoImage(file="resourses//images//btn_calification.png",master=self)
        btn_update_calification = Button(image=file_update_calification,width=150,height=150,master=self,command=self.Update_calification_app)
        btn_update_calification.place(x=650, y=220)
        self.mainloop()

    def Delete_menu(self):
        self = App()
        self.title("Delete Menu")
        file_delete_student=PhotoImage(file="resourses//images//btn_delete_student.png",master=self)
        btn__new_student = Button(image=file_delete_student,width=150,height=150,master=self,command=self.Delete_student)
        btn__new_student.place(x=430, y=220)
        file_delete_course=PhotoImage(file="resourses//images//btn_delete_course.png",master=self)
        btn_delete_course = Button(image=file_delete_course,width=150,height=150,master=self,command=self.Delete_course)
        btn_delete_course.place(x=650, y=220)
        self.mainloop()
    
    def Create_student_app(self):
        self=App()
        self.title("App Create Student")
        title = Label (self,text="Favor llene los espacios con la información solicitada:", font=("Adobe Gothic Std B",24),background="white").place(x=200,y=15)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_carnet.place(x=370,y=75)
        lbl_course = Label (self,text="Digite el curso que desea agregar al estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=135)
        ent_course= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_course.place(x=535,y=135)
        lbl_name = Label (self,text="Digite el nombre del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=195)
        ent_name= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_name.place(x=384,y=195)
        lbl_direction = Label (self,text="Digite la dirección del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=255)
        ent_direction= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_direction.place(x=399,y=255)
        lbl_telephone = Label (self,text="Digite el telefono del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=315)
        ent_telephone= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_telephone.place(x=390,y=315)
        lbl_email = Label (self,text="Digite el email del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=375)
        ent_email= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_email.place(x=364,y=375)

        #ERROR EN EL SAVE
        def save():
            self.student.set_carnet(ent_carnet.get())
            self.student.set_course(ent_course.get())
            self.student.set_name(ent_name.get())
            self.student.set_direction(ent_direction.get())
            self.student.set_telephone(ent_telephone.get())
            self.student.set_email(ent_email.get())
            self.db.set_information(self.student.get_information())

        save = Button(self,text="GUARDAR",font=('Arial 20'),command=save).place(x=100,y=500)
        self.mainloop()

    def Create_course_app(self):
        self=App()
        self.title("App Create Course")
        title = Label (self,text="Favor llene los espacios con la información solicitada:", font=("Adobe Gothic Std B",24),background="white").place(x=200,y=15)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_carnet.place(x=370,y=75)
        def found():
            if  self.db.found_carnet(ent_carnet.get()):   
                lbl_course = Label (self,text="Digite el curso que desea agregar al estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=135)
                ent_course= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_course.place(x=535,y=135)
                def found_course():
                    if self.db.found_course(ent_carnet.get(),ent_course.get()):
                        messagebox.showinfo(title="Error", message="El curso ya se encuentra en la base de datos " + " del estudiante " + ent_carnet.get())
                    else:
                        self.db.add_course(ent_carnet.get(),ent_course.get())
                        messagebox.showinfo(title="Éxito", message="El curso " + str(ent_course.get()) + " fue agregado correctamente" + "al estudiante " + str(ent_carnet.get()))
                found_course = Button(self,text="AGREGAR",height=1,width=12,font=('Arial 9'),command=found_course).place(x=970,y=137)
            else:
                messagebox.showinfo(title="Error", message="El carnet "+ent_carnet.get() + " no se encuentra en la base de datos ")
                
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=810,y=78)

        self.mainloop()

    def Read_studens_app(self):
        self=App()
        self.title("App Read Students")
        #VALIDAR SI NO HAY ESTUDIANTES MOSTRAR UN MENSAJE DE QUE NO HAY
        title = Label (self,text="La información de todos los estudiantes se muestra en el siguiente recuadro:", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        text_students = tk.Text(self, height=37, width=140)
        scroll_bar = tk.Scrollbar(self)
        scroll_bar.pack(side=tk.RIGHT)
        text_students.pack(side=tk.LEFT)
        long_text = str(self.db.get_students())
        text_students.insert(tk.END, long_text)
        mainloop()
    
    def Read_student_app(self):
        self=App()
        self.title("App Read Student")
        title = Label (self,text="Favor ingrese el carnet del estudiante del que desea ver la información", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_carnet.place(x=370,y=75)
        def found():
            if  self.db.found_carnet(ent_carnet.get()):
                text_student = tk.Text(self, height=15, width=140,font=('Arial 16'))
                scroll_bar = tk.Scrollbar(self)
                scroll_bar.pack(side=tk.RIGHT)
                text_student.pack(side=tk.LEFT)
                long_text = str(self.db.get_student(ent_carnet.get()))
                text_student.insert(tk.END, long_text)
            else:
                messagebox.showinfo(title="Error", message="El carnet "+ ent_carnet.get() + " no se encuentra en la base de datos ")
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=800,y=75)

    def Read_courses_app(self):
        self=App()
        self.title("App Read Courses")
        title = Label (self,text="Favor ingrese el carnet del estudiante del que desea ver la información de los cursos matriculados", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_carnet.place(x=370,y=75)
        def found():
            if  self.db.found_carnet(ent_carnet.get()):
                text_student = tk.Text(self, height=15, width=140,font=('Arial 16'))
                scroll_bar = tk.Scrollbar(self)
                scroll_bar.pack(side=tk.RIGHT)
                text_student.pack(side=tk.LEFT)
                long_text = str(self.db.get_courses(ent_carnet.get()))
                text_student.insert(tk.END, long_text)
            else:
                messagebox.showinfo(title="Error", message="El carnet "+ ent_carnet.get() + " no se encuentra en la base de datos ")
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=800,y=75)
    
    def Update_information_app(self):
        self=App()
        self.title("App Update Information")
        title = Label (self,text="Llene los espacios con la información que desea actualizar", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante al que desea cambiarle la información: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=15)
        ent_carnet.place(x=750,y=75)
        def found():
            if  self.db.found_carnet(ent_carnet.get()):
                lbl_name = Label (self,text="Digite el nombre del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=195)
                ent_name= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_name.place(x=384,y=195)
                lbl_direction = Label (self,text="Digite la dirección del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=255)
                ent_direction= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_direction.place(x=399,y=255)
                lbl_telephone = Label (self,text="Digite el telefono del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=315)
                ent_telephone= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_telephone.place(x=390,y=315)
                lbl_email = Label (self,text="Digite el email del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=375)
                ent_email= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_email.place(x=364,y=375)
                def set_information():
                    self.db.change_information(ent_carnet.get(),ent_name.get(),ent_direction.get(),ent_telephone.get(),ent_email.get())
                    messagebox.showinfo(title="Éxito", message="La informacion del estudiante "+ent_carnet.get() + " fue actualizada ")
                set_information = Button(self,text="ACTUALIZAR",height=1,width=12,font=('Arial 9'),command=set_information).place(x=760,y=450)
            else:
                messagebox.showinfo(title="Error", message="El carnet "+ ent_carnet.get() + " no se encuentra en la base de datos ")
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=950,y=77)

    
    def Update_calification_app(self):
        self=App()
        self.title("App Update Calification")
        title = Label (self,text="Llene los espacios con la información solicitada", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante al que desea cambiarle la nota: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=15)
        ent_carnet.place(x=680,y=75)
        def found():
            if  self.db.found_carnet(ent_carnet.get()):   
                lbl_course = Label (self,text="Digite el curso que desea agregar al estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=135)
                ent_course= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_course.place(x=535,y=135)
                def found_course():
                    if self.db.found_course(ent_carnet.get(),ent_course.get()):
                        lbl_calification = Label (self,text="Digite la nota que desea asignarle al curso ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=195)
                        ent_calification = Entry(self,font=("Adobe Gothic Std B",16),width=15)
                        ent_calification.place(x=500,y=197)
                        def set_calification():
                            self.db.set_calification(ent_carnet.get(),ent_course.get(),ent_calification.get())
                        set_calification = Button(self,text="ACTUALIZAR",height=1,width=12,font=('Arial 9'),command=set_calification).place(x=760,y=300)
                        messagebox.showinfo(title="Éxito", message="La nota del curso "+ent_course.get() + " fue actualizada ")

                    else:
                        messagebox.showinfo(title="Error", message="El curso " + str(ent_course.get()) + " no se encuentra agregado al estudiante " + str(ent_carnet.get()))
                found_course = Button(self,text="BUSCAR CURSO",height=1,width=12,font=('Arial 9'),command=found_course).place(x=970,y=137)
            else:
                messagebox.showinfo(title="Error", message="El carnet "+ent_carnet.get() + " no se encuentra en la base de datos ")
                
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=880,y=78)

    def Delete_student(self):
        self=App()
        self.title("App Delete Student")
        title = Label (self,text="Favor ingrese el carnet del estudiante del que desea ver la información", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=35)
        ent_carnet.place(x=370,y=75)
        def found():
            if  self.db.found_carnet(ent_carnet.get()):
                self.db.delete_student(ent_carnet.get())
                messagebox.showinfo(title="Éxito", message="El estudiante con carnet "+ ent_carnet.get() + " ha sido eliminado ")
            else:
                messagebox.showerror(title="Error", message="El carnet "+ ent_carnet.get() + " no se encuentra en la base de datos ")
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=800,y=75)

    def Delete_course(self):
        self=App()
        self.title("App Delete Course")
        title = Label (self,text="Llene los espacios con la información solicitada", font=("Adobe Gothic Std B",24),background="white").place(x=10,y=3)
        lbl_carnet = Label (self,text="Digite el carnet del estudiante al que desea eliminarle el curso: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=75)
        ent_carnet= Entry(self,font=("Adobe Gothic Std B",16),width=15)
        ent_carnet.place(x=680,y=75)
        
        def found():
            if  self.db.found_carnet(ent_carnet.get()):   
                lbl_course = Label (self,text="Digite el curso que desea eliminar: ", font=("Adobe Gothic Std B",16),background="white").place(x=50,y=135)
                ent_course= Entry(self,font=("Adobe Gothic Std B",16),width=35)
                ent_course.place(x=535,y=135)
                def found_course():
                    if self.db.found_course(ent_carnet.get(),ent_course.get()):
                        self.db.delete_course(ent_carnet.get(),ent_course.get())
                        messagebox.showinfo(title="Éxito", message="El curso "+ent_course.get() + " ha sido eliminado ")
                    else:
                        messagebox.showerror(title="Error", message="El curso " + str(ent_course.get()) + " no se encuentra agregado al estudiante " + str(ent_carnet.get()))
                found_course = Button(self,text="BUSCAR CURSO",height=1,width=12,font=('Arial 9'),command=found_course).place(x=970,y=137)
            else:
                messagebox.showerror(title="Error", message="El carnet "+ent_carnet.get() + " no se encuentra en la base de datos ")
                
        found = Button(self,text="BUSCAR",height=1,width=10,font=('Arial 9'),command=found).place(x=880,y=78)

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

db =Data_Base()
