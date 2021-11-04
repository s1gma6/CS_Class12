def bubsort(L):
    n = len(L)
    for i in range(n-1):
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


n = int(input("Enter no of elements in list:"))
L = []
for i in range(n):
    a = int(input("Enter element/s:"))
    L.append(a)
print("Original List:", L)
bubsort(L)
print("Sorted list is:", L)
