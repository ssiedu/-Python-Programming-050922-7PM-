file = open("Student.txt","w")
for i in range(3):
    name=input("Enter Name : ")
    rollno = int(input("Enter student roll no : "))
    marks = eval(input("Enter marks : "))
    data= name +"\n" + str(rollno) + "\n" + str(marks)+"\n"
    file.write(data)
file.close()
