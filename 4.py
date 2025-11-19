def numbers(n):
    if n == 1:
        return a
    else:
        print(a-n+1)
        return numbers(n-1)
a = int(input('Enter number: '))
print(numbers(a))
