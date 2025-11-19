a = int(input('Enter Your number to check whether it is a magic number:'))
b=0
c=0
n=0
d=0
while a >0:
    b=b+(a%10)**2
    a=a//10
    while b > 10:
        c=c+(b%10)**2
        b=b//10
    if c ==1:
        print('It is a happy number')
        n=1
        break
    elif a<10 and b==1:
        print('It is an happy number')
        n=1
        break
    while c > 10:
        d=d+(c%10)**2
        c=c//10
    if d ==1:
        print('It is a happy number')
        n=1
        break
if n==0:
    print('Not an happy number')

        
