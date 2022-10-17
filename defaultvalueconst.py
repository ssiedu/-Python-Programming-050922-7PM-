class Student:
    def __init__(self,name="sita",age=12,rno=2022):
        self.name=name
        self.age=age
        self.rollno=rno

    def display(self):
        print("Student Name : ", self.name)
        print(" Student Age : ", self.age)
        print(" Student Roll No : ",self.rollno)


s=Student(age=22,rno=1011)
s.display()
s1=Student("Shyam",23,1022)
s1.display()
s2=Student()
s2.display()
