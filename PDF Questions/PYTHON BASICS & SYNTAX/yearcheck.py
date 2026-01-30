n = int(input("Enter the year: "))
if n%4 == 0:
    if n%100 == 0 and n%400 != 0:
        print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
