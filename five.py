n = int(input("Enter Your number: "))
p=[]
a = 0
for i in range (1,n):
    a = 0
    for j in range (2,i):
        if i%j == 0:
            a=1
            break
    if a == 0:
        p.append(i)
p.sort()
print('Largest prime less than {} is {}'.format(n,p[-1]))
print(p)
