class Base:
    def __init__(self):
        self.x=int(input("Enter the value of x : "))
        self.y=int(input("Enter the value of y : "))


class derive1(Base):
    def getSum(self):
        self.add=self.x+self.y
        print("Addition of two numbers : ",self.add)


class derive2(Base):
    def getMul(self):
        self.mul=self.x*self.y
        print("Multiplication of two Numbers : ",self.mul)


class derive3(Base):
    def getDiv(self):
        self.div= self.x/self.y
        print("Division of Number : ", self.div)


d1=derive1()
d1.getSum()

d2=derive2()
d2.getMul()

d3=derive3()
d3.getDiv()
