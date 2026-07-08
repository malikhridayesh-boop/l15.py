L = [4,5,1,2,9,7,10,8]
print("Original List:", L)
sum = 0
for i in L:
    sum += i
avg = sum / len(L)
print("sum = ",sum)
print("average = ", avg)
L.sort()
print("smallest number in the list:", L[0])
print("largest number in the list:", L[-1])