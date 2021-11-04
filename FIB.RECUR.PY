def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1)+fib(n-2))


n = int(input("Enter number of terms:"))
if n <= 0:
    print("Enter only Positive Integers")
else:
    print("fib Sequence:")
    for i in range(n):
        print(fib(i))
