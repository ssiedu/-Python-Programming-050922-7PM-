class Student:
    def __init__(self):
        self.name="Aman"
        self.age = 12
        self.rollno = 101
    def __init__(self):
        
        self.name="Ram"
        self.age=11
        self.rollno=102

    def display(self):
        print("Student Name : ", self.name)
        print(" Student Age : ", self.age)
        print(" Student Roll No : ",self.rollno)


s=Student()
s.display()
s1=Student()
s1.display()
