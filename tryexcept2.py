try:
    #a=5
    b='0'
    print(a+b)
except TypeError:
    print("Unsupported Operation ")
except NameError:
    #print("Name Error Occured ")
    pass

print("Out of try except block")
