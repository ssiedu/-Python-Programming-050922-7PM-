p=int(input("Enter principal amount :"))
r=int(input("Enter rate of interest :"))
t=int(input("Enter time period :"))
simple_interest=(p*r*t)/100
print("simple interest = ",simple_interest)
total_amount=p+simple_interest
print("Total amount = ",total_amount)
