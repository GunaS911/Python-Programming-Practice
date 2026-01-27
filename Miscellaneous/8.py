n = int(input("Enter the number:"))
b = n
a = 0
while b >0:
    a = a*10+b%10
    b = b//10
print("The reverse of {} is {}".format(n,a))
