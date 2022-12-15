
# Sorting integer array using pointers

arr = [1,3,2,4]
arr1 = []
for i in arr:
    arr1.append(i)
print(sorted(arr1))

## Traverse through all array elements
arr = [7,9,2]

for i in range(len(arr)):
    min_idx = i
    # Find the minimum element in remaining unsorted array
    for j in range(i+1,len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    # Swap the found minimum element with
    # the first element
    arr[i],arr[min_idx] = arr[min_idx],arr[i]
print(arr)

