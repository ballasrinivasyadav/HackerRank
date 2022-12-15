
# Sort an array
arr = [2,3,5,7,9,1,4,6]
temp = 0
print("Elements of original array:")
for i in range(0,len(arr)):
    print(arr[i],end=' ')

# Sorting arrays in ascending order
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print()

print("Elements after sorting ")
for i in range(0,len(arr)):
    print(arr[i],end=' ')


# New method

arr = [12,11,6,1,2]

for i in range(0,len(arr)):
    for j in range(i+1,)