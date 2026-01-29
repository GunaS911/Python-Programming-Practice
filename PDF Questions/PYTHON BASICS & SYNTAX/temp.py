while True:
    a = int(input("Enter 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celcius"))
    if a==1:
            c = int(input("Enter the temperature in Celsius: "))
            f = c*(9/5) + 32
            print("{}F".format(f))
            break
    elif a==2:
            f = int(input("Enter the temperature in fahrenheit: "))
            c = 5/9*(f-32)
            print("{}C".format(c))
            break
    else:
        print("Enter a valid option")

