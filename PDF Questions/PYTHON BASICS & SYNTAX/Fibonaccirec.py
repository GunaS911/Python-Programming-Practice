n=int(input("Enter the number of terms: "))
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2)+fibo(n-1)
for i in range(0,n+1):
    print(fibo(i))
