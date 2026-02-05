n=int(input("Enter your number: "))
for i in range(2,n):
    if n%i==0:
        a=0
        print("{} is not a prime".format(n))
        break
    elif i==n-1:
        print("{} is a prime".format(n))
if n==2:
    print("{} is a prime".format(n))
