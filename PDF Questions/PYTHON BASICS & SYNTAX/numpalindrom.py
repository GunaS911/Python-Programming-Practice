import math
n = int(input("Enter your number: "))
ni = n
nn=0
ln=[]
while n>0:
    ln.append(n%10)
    n=n//10
for i in range(0,len(ln)):
    nn=nn+ln[i]*pow(10,len(ln)-i-1)
if nn==ni:
    print("Palindrome")
else:
    print("Not Palindrome")
