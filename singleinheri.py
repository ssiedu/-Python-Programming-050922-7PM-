class Base:
    def getdata(self):
        self.x=int(input("Enter the value of x : "))
        self.y=int(input("Enter the value of y : "))


class derive(Base):
    def calculate(self):
        self.add=self.x+self.y
    def display(self):
        print("Addition of two numbers : ", self.add)


d=derive()
d.getdata()
d.calculate()
d.display()
