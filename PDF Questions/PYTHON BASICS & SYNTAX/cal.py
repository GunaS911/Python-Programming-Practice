while True:
    o = int(input("Enter 1 for add,2 for subtract,3 for multiply,4 for division and 5 for quit: "))
    if o==5:
        break
    n = int(input("Enter the first number(larger one): "))
    a = int(input("Enter the second number: "))
    if o ==1:
        print("Addition = ",n+a)
    elif o==2:
        print("Subtraction = ",n-a)
    elif o==3:
        print("Multiplication =",n*a)
    elif o==4:
        print("Division =",n/a)

