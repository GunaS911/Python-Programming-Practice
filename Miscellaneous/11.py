a=0
b=0
n = int(input('Enter the range to find the armstrong number: '))
for i in range (n+1):
    b=i
    a=0
    while b >0:
        a=(b%10)**3 + a
        b=b//10
    if a == i:
        print(i)

