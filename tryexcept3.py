try:
    a=5
    b=0
    print(a/b)

except TypeError:
    print("Unsupported Operation")

except ZeroDivisionError:
    print("Division by Zero not allowed")

except:
    print("Some Error Occured")


print("Out of try except block")
