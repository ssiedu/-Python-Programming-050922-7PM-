class Student:
    def getdata(self):
        self.name=input("Enter student Name : ")
        self.rollno=int(input("Ener Student roll no:"))
        self.marks = eval(input("Enter Student Percentage : "))
    def display(self):
        print("student Name : ",self.name)
        print("Student roll no : ",self.rollno)
        print("Student percentage : ",self.marks)


S1=Student()
S1.getdata()

S2=Student()
S2.getdata()
S1.display()
S2.display()
        
