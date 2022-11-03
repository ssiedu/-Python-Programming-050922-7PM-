try:
    x=int(input("Enter a number upto 100 :"))
    if x>100:
        raise ValueError(x)
        

except ValueError:
    print(x,"is out of range")



else:
    print(x,"is in range")
