class Base1:
    def __init__(self,a):
        self.x=a


class Base2:
    def getdata(self,b):
        self.y=b


class derive(Base1,Base2):
    def putdata(self):
        self.add=self.x+self.y
        print("addition of two numbers :",self.add)

x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
d=derive(x)
d.getdata(y)
d.putdata()
