import random
a = random.randint(0,101)
at =1
while True:
    b = int(input("Enter a guess from 0,100: "))
    if a!=b:
        print("try again")
        at +=1
    else:
        print("correct guess")
        print("No of attempts: ",at)
        break

