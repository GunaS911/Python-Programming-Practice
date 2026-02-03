n=int(input("Enter your number:"))
c=0
while n>0:
    n=n//10
    c+=1
print("Number of digits:",c)
