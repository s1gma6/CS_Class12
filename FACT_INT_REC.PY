def factorial(a):
    if(a == 1):
        return 1
    else:
        return a*factorial(a-1)


n = int(input("Enter a number:"))
if(n < 0):
    print("factorial does not Exist for negative numbers")
elif(n == 0):
    print("factorial of zero is 1")
else:
    print("The factorial of", n, "is:", factorial(n))
