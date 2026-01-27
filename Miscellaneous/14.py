n = int(input('Enter the number: '))
a=1
d=0
x=0
for i in range(1,n+1):
    a=a*i
while True:
    d=a%10
    a=a//10
    if d == 0:
        x=x+1
    else:
        print('The number of Trailing zeros of {}! is {}'.format(n,x))
        break

