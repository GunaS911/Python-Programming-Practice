n = int(input("Enter the first number: "))
ni = int(input("Enter the second number: "))
for i in range(1,n*ni+1):
    if i%n == 0 and i%ni == 0:
        print("{} is the LCM".format(i))
        break
