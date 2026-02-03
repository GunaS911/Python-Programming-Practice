import math
n = int(input("Enter your number: "))
ln=[]
nn=0
while n>0:
    ln.append(n%10)
    n=n//10
for i in range(0,len(ln)):
    nn=nn+ln[i]*pow(10,len(ln)-i-1)
print("Reversed number:",nn)
