class Base:
    def print(self):
        print("Inside print method in Base class ")

    def show(self):
        print("Inside Show method in Base class")

class Derive(Base):
    def print(self):
        Base.print(self)
        print("Inside print method in derive class")

    def show(self):
        Base.show(self)
        print("Inside show method in derive class")


d=Derive()
d.print()
d.show()
