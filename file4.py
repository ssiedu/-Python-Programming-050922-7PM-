file = open("demo.png","rb")
fout = open("picture.png","wb")
#str = file.read()
#for i in str:
#print(i,end=" ")
fout.write(file.read())
file.close()
fout.close()
