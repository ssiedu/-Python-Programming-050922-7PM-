num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
ch=input("Enter Choice like (+,-,*,/)")

match ch:
      case '+':
            print("sum is : ",num1+num2)
      case '-':
            print("sub is : ",num1-num2)
      case '*':
            print("Mul is : ",num1*num2)
      case '/':
            print("Div is : ",num1/num2)
      case _:
            print("Invalid choice")
            
