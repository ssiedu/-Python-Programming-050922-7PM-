class addition:
    def getdata(self,num1,num2):
        self.n1=num1
        self.n2=num2
    def add(self):
        self.sum=self.n1+self.n2
    def display(self):
        print("Addition of two numbers : ",self.sum)


a1=addition()
a1.getdata(2,3)
a2=addition()
a2.getdata(10,20)
a1.add()
a2.add()
a1.display()
a2.display()
