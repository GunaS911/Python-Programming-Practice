def number(N):
    if N>0:
        number(N-1)
        print(N)
n = int(input('Enter Number: '))
number(n)
