import random
while True:
    uc=int(input('''
Game Start....
1.Yes
2.No|Exit
Enter Choice : '''))
    if uc==1:
        Cnumber = random.randrange(1,4)
        Userinput = int(input("Enter your number : "))
        if Userinput > Cnumber:
            print("Computer number  ",Cnumber)
            print("Your guess number is too high")
        elif Cnumber>Userinput:
            print("Computer number ", Cnumber)
            print("Your guess number is too low")
        else:
            print("Computer number ",Cnumber)
            print("Your guess number is equal")
    else:
        break;
