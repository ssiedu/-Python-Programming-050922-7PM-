class factorial:
    
    def getdata(self,n):
        self.num=n
    def calculate(self):
        self.fact=1
        for i in range(self.num):
            self.fact=self.fact*(i+1)
    def display(self):
        print("factorial of a number : ",self.fact)


f=factorial()
f.getdata(5)
f.calculate()
f.display()
