class Base:
    def fun1(self):
        print("This is a Base class")


class derive(Base):
    def fun2(self):
        print("This is a derive class")


d=derive()
d.fun1()
d.fun2()
