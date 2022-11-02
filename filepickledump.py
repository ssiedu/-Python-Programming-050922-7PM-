import pickle
file = open("binary.dat","wb")
x=[10,20,30,40,50]
pickle.dump(x,file)
file.close()
file = open("binary.dat","rb")
data=pickle.load(file)
print(data)
file.close()
