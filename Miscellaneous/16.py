a=input('Enter your string: ')
b=a.split(' ')
print(b)
l=1
g=''
c=[]
for i in b:
    if i not in c:
        c.append(i)
    for j in c:
        l=1
        for k in range(0,len(c)):
            if len(j) > len(c[k]) and l==1:
                l=1
                g=j
            else:
                l=0

print(g,len(g))



