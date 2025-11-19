a = input('Enter your string: ')
v='aeiouAEIOU'
r=''
re=[]
for i in a:
    if i in v:
        re.append(i)
re.reverse()
c=-len(re)
for i in a:
    if i in v:
        r=r+re[c]
        c=c+1
    else:
        r=r+i
print(r)
print(re)
