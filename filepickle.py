import pickle
class Student:
    def __init__(self,rno=0,name= " "):
        self.rollno = rno;
        self.name  =name
        self.s1,self.s2,self.s3 = 0.0,0.0,0.0
    def readMarks(self):
        print("Enter Marks of Student : ")
        self.s1=eval(input("Enter Marks of subject1 : "))
        self.s2=eval(input("Enter Marks of Subject2 : "))
        self.s3=eval(input("Enter marks of subject 3 :"))
    def display(self):
        print("Roll No : ", self.rollno)
        print("Name    : ", self.name)
        print(" Subject 1 : ", self.s1)
        print(" Subject 2 : ", self.s2)
        print(" Subject 3 : ", self.s3)

S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.readMarks()
S2.readMarks()
fout = open("Record","wb")
pickle.dump(S1,fout)
pickle.dump(S2,fout)
fout.close()
file=open("Record","rb")
#S1=pickle.load(file)
#S2=pickle.load(file)
#print(S1.__dict__)
#print(S2.__dict__)
try:
    while True:
        s=pickle.load(file)
        s.display()
except:
    file.close()





