def List(m, n):
    if(n == 0):
        return 0
    else:
        return m[n-1]+List(m, n-1)


x = int(input("Enter the number of elements for list:"))
m = []
for i in range(0, x):
    num = int(input("Enter element:"))
    m.append(num)
print("The list is:", m)
print("Sum of items in list:")
sum = List(m, x)
print(sum)
