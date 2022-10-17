class Student:
    def __init__(self):
        self.name = input("Enter Student Name : ")
        self.age = int(input("Enter Student Age : "))
        self.id  = int(input("Enter Student id : "))
    def display(self):
        print("Student Name : ", self.name)
        print("Student age  : ", self.age)
        print("Student Id   : ", self.id)


s=Student()
s.display()
