a = input('Enter your str: ')
l=[]
c=''
for i in a:
    if i not in l:
        l.append(i)
        b=a.count(i)
        l.append(i+str(b))
for j in range (0,len(l)):
    if j%2 !=0:
        c=c+l[j]
print(c)
