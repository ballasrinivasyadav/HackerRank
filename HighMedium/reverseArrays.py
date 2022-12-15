# Reverse the array elements
# array = [1,2,3,4,5]
         # 0 1 2 3 4
         # i       j
         # l = len(array) ==== 5

# rev_array = [5,4,3,2,1] ==== Output

# Reversing a list using two-pointer approach

def rev_list1(array):
    n = len(array)
    i = 0
    j = n - 1
    while i < j:  # Swap
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    return array

array = [1, 2, 3, 4, 5]

print(rev_list1(array))


def rev_list1(array):
    left = 0
    right = len(array) - 1  # Length of array is:5-1=4
    while left < right:  #
        # Swap
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        left += 1
        right -= 1
    return array
array = [1, 2, 3, 4, 5]
print(len(array)-1)
print("reversed function is:", rev_list1(array))

def rev_list1(arr):
    n = len(arr)
    first = 0
    last = n-1
    while first<last:
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp
        first+=1
        last-=1
    return arr
arr = [11,12,13,14,15]
print(rev_list1(arr))



arr = [1,4,5,6,8]
n = len(arr)
i = 0
j = n-1
while i<j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i+=1
    j-=1
print(arr)
