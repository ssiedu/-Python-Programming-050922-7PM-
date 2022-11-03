try:
    print("Try Block")
    x=int(input("Enter First Number : "))
    y=int(input("Enter Second Number : "))
    z=x/y

except ZeroDivisionError:
    print("Division by Zero not allowed")

else:
    print("Else block")
    print("Division = ",z)

finally:
    print("Finally Block")

print("Out of try except else and finally")
