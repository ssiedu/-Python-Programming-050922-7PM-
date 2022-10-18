class Base:
    def __init__(self):
        self.x=int(input("Enter the value of x : "))
        self.y=int(input("Enter the value of y : "))


class Intermediate(Base):
    def calculate(self):
        self.add=self.x+self.y


class derive(Intermediate):
    def display(self):
        print("addition of two numbers : ",self.add)


d=derive()
#d.getdata()
d.calculate()
d.display()
