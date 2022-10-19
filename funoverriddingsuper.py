class Base:
    def print(self):
        print("Inside print method in Base class ")

    def show(self):
        print("Inside Show method in Base class")

class Derive(Base):
    def print(self):
        super().print()
        print("Inside print method in derive class")

    def show(self):
        super().show()
        print("Inside show method in derive class")


d=Derive()
d.print()
d.show()
