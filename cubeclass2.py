class Cube:
    def getdata(self,n):
        #self.num=int(input("Enter Any Number : "))
        self.num=n
    def calculate(self):
        self.res=self.num*self.num*self.num
    def display(self):
        print("cube of number : ",self.res)

c1=Cube()
num=int(input("Enter Any Number : "))
num1=int(input("Enter Any Number : "))
c1.getdata(num)
c2=Cube()
c2.getdata(num1)

c1.calculate()
c1.display()
c2.calculate()
c2.display()
