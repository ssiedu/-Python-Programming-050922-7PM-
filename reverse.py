num=int(input("Enter any number : "))
rev=0
count=0
sod=0
temp=num
while num>0:
      rev=rev*10+num%10
      sod=sod+num%10
      num= num//10
      count=count+1
print("reverse number is ", rev)
print("Total number of digit : ",count)
print(" sum of digit : ", sod)
#print("Number is " , num)
if temp==rev:
      print("Number is pallindrome")
else:
      print("Number is not pallindrome")
