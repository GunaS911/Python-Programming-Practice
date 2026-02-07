n = int(input("Enter the number of lines: "))
#pyramids
for i in range(0,n+1):
    for j in range(0,i+1):
        print("*",end='')
    print(" ")
#diamond
for i in range(0,n+1):
    if (i>n//2):
        print(" "*i ,end =' ')
        print("*"*(n+1-i))
    else:
        print(" "*(n-i+1),end= ' ')
        print("*"*i)
#triangle
for i in range(0,n+1):
    print(" "*((n-i+1)//2),end='')
    print("*"*(i+1))

