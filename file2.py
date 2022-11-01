file=open("Mydata","w")
list1=[]
for i in range(5):
    name=input("Enter Name of student : ")
    list1.append(name+"\n")


file.writelines(list1)
file.close()
print(name)
