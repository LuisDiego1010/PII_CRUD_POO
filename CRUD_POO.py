import shelve
students=[]
archive = "students_base"
loop = True
from tkinter import *

class Student():
    carnet=0
    name=""
    direction=""
    telephone=0
    email=""
    cursos={}
    
    def Create(self):
        self.carnet=int(input("Ingrese el número de carnet del/la estudiante: "))
        self.name=str(input("Ingrese el nombre del/la estudiante: "))
        self.direction=input("Ingrese la dirección del/la estudiante: ")
        self.telephone=int(input("Ingrese el teléfono del/la estudiante: "))
        self.email=str(input("Ingrese el correo electrónico del/la estudiante: "))
        cursos={["CA2109",0],["DT2145",0]}
        cursos=[["CA2109",0],["DT2145",0]]
        print("\nEl estudiante fue creado")
    

    def get_carnet(self):
        return self.carnet

    def Read(self):
        print(self.carnet)
        print(self.name)
        print(self.direction)
        print(self.telephone)
        print(self.email)
    
e1=Student()
e1.Create()
e1.Read()

e2=Student()
e2.Create()
e2.Read()

students.append(e1)
students.append(e2)

for i in students:
    print ("El carnet del estudiante: " + str(i.carnet))

