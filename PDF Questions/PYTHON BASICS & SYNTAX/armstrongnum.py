import math
n = int(input("Enter the number: "))
ni=0
nn=n
while n>0:
    ni=ni+pow((n%10),3)
    n=n//10
if(ni==nn):
    print("Its an armstrong number")
else:
    print("Not an armstrong number")
