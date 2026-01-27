n = int(input('Enter Your number : '))
a=0
b=0
c=0
for i in range (0,n+1):
    b = i
    a=0
    c=0
    while b > 0 :
        a = a+b%10
        b = b//10
    if a >= 10:
        while a > 0 :
            c = c + a%10
            a=a//10
        if c ==1:
            print('{} is a magic number'.format(i))
    if a == 1:
            print('{} is a magic number'.format(i))
            
            
