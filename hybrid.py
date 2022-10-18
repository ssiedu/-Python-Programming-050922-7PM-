class Base:
    def getdata(self):
        self.x=int(input("Enter the value of x : "))
        self.y=int(input("Enter the value of y : "))

class derive1(Base):
    def getSum(self):
        self.add=self.x+self.y


class Base2:
    def getValue(self):
        self.x=int(input("Enter the value of x : "))
        self.y=int(input("Enter the value of y : "))

    def getMul(self):
        self.mul= self.x*self.y


class child(derive1,Base2):
    def display(self):
        print("Addition : ", self.add)
        print("Multiplication : ", self.mul)

C1=child()
C1.getdata()
C1.getSum()
C1.getValue()
C1.getMul()
C1.display()

        
