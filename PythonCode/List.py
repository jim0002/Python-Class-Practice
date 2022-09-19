arr1 = [10, 20, 23, 11, 17]
arr2 = [13, 43, 24, 36, 12]
arr = []
# adding odd
for i in arr1:
    if(i % 2!=0):
        arr.append(i)
# adding even
for i in arr2:
    if (i % 2 ==0):
        arr.append(i)
print("\nList of odd and even numbers: ", arr)

# sorting the list bubble
size = len(arr)
for i in range(size):
    for j in range (0, size - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("\nAfter final sorting : ", arr)
