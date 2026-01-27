n = int(input('enter the number of rows: '))
t = []
r = []
for i in range (n):
    r = [1]*(i+1)
    for j in range (1,i):
        r[j] = t[i-1][j-1]+t[i-1][j]
    t.append(r)
print(t)
