class Student:
    def __init__(self,name,age,rno):
        self.name=name
        self.age=age
        self.rollno=rno

    def display(self):
        print("Student Name : ", self.name)
        print(" Student Age : ", self.age)
        print(" Student Roll No : ",self.rollno)


s=Student("Ram",22,1011)
s.display()
s1=Student("Shyam",23,1022)
s1.display()
