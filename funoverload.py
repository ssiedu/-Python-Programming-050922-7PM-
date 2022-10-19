class Area:
    def findArea(self,num1=None,num2=None):
        if(num1!=None and num2!=None):
            print("Area of rectangle : ",num1*num2)
        elif(num1!=None):
            print("Area of Square : ", num1*num1)
        else:
            print("Nothing is Here ")


A=Area()
A.findArea(2,3)
A.findArea(5)
A.findArea()


