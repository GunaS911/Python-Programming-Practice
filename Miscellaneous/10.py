n = int(input('Enter your number to be checked: '))
c=0
for i in range(0,n):
    for j in range(0,n):
        if i**2 + j**2 == n:
            print('{} can be represented as sum of squares of {} and {}'.format(n,i,j))
            c=1
    if c==1:
        break
if c==0:
    print("Cannot be represented as sum of squres")
 
