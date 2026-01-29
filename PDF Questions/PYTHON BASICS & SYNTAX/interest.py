import math
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period in years: "))
s =(p*r*t)/100
c=0
while (t)>0:
    c = ((p*r)/(100))+c
    p = ((p*r)/(100))+p
    t-=1
print("The simple interest is {} and the compound interest is {}".format(s,c))

