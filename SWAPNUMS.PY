def SwapNumbers(x, y):
    print("Numbers before swapping are:", x, "and", y)
    x, y = y, x
    print("Numbers after swapping are:", x, "and", y)


x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
SwapNumbers(x, y)
