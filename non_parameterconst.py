class Student:
    def __init__(self):
        self.name = "Ram";
        self.age = 22;
        self.id  = 101;
    def display(self):
        print("Student Name : ", self.name)
        print("Student age  : ", self.age)
        print("Student Id   : ", self.id)


s=Student()
s.display()
