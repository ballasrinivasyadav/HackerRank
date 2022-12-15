# Binary search
def Binary_search(list1, low, high, index):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if list1[mid] == index:
            return mid
        # If element is smaller than mid,then it can only be present in left subarray
        elif list1[mid] > index:
            return Binary_search(list1, low, mid - 1, index)
        # Else the element can only be present in right subarray
        else:
            return Binary_search(list1, mid + 1, high, index)
    else:
        return -1


# Test array
list1 = [2, 3, 4, 10, 40]
index = 10
# Function call
result = Binary_search(list1, 0, len(list1) - 1, index)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
print(4 + 6 // 2)


def Binary_search(list2, low, high, index):
    if low <= high:
        mid = (low + high) // 2  # 7
        if list2[mid] == index:  # [10,7,1,4,23,100,18]  #Fails
            return mid
        elif index > list2[mid]:   #
            return Binary_search(list2, mid - 1, high, index)
        else:
            return Binary_search(list2, low, mid + 1, index)
    else:
        return -1


list2 = [10, 7, 1, 4, 23, 100, 18]
# list2.sort()
index = 1
n = len(list2)
low = 0
high = len(list2) - 1
print(list2)
result = Binary_search(list2, low, high, index)
if result != -1:
    print("Element is present at index:", str(result))
else:
    print("Elements not found in list2")
