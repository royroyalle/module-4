L = [2, 5, 6, 9, 3, 1]
print("Org list:", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("sum:", count)
print("average:", avg)
L.sort()
print("Sorted list:", L)
print("Smallest Number from list:", L[0])
print("Largest Number from list:", L[-1])