def linearsearch(L, x):
    for i in range(len(L)):
        if L[i] == x:
            c = 1
            return c


n = int(input("Enter no of elements to put in list:"))
r = []
for i in range(n):
    a = int(input("Enter element:"))
    r.append(a)
t = int(input("Enter the element to be searched:"))
a = linearsearch(r, t)
if(a == 1):
    print("Element Found Sucessfully")
else:
    print("Element Not Found")
