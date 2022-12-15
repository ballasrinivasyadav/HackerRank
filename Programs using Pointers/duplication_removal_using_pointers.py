
# duplication removal using pointers
lst = [1,2,1,3,3]
print(set(lst))
#For loop
#
res1 = []
for i in lst: #lst = [1,2,1,3,3]
    if i not in res1:
        res1.append(i)
print(res1)
#

#Recursive method
def dupl(lst):
    return list(set(lst))
print(dupl(lst))
# For loop
set1 = []
for i in lst:
    set1.append(i)
print(list(set(set1)))
# Functions
set2 = []
def dupli(lst):
    for i in lst:
        set2.append(i)
    print(list(set(set2)))
dupli(lst)
# List Comprehensions
res = []
[res.append(i) for i in lst if i not in res]
print(res)

# Functions Methods


def removeDuplicates(lst,n):
    # if n == 0 or n == 1:
    #     return n
    res1 = list(range(n))
    j = 0
    for i in range(0,n-1):
        if lst[i] != lst[i+1]:
            res1[j] = lst[i]
            j=j+1
    res1[j] = lst[n-1]
    j=j+1
    for i in range(0,j):
        lst[i] = res1[i]
    return j
lst = [1,2,2,3,3,5,5,4,4]
lst.sort()
n = len(lst)
n = removeDuplicates(lst,n)
for i in range(n):
    print((lst[i]),end=" ")

#
print('\n')
def remove_Duplicate(arr,n):
    j = 0
    res1 = list(range(n))
    for i in range(0,n-1):
        if arr[i] != arr[i+1]:
            res1[j] = arr[i]
            j = j+1

    res1[j] = arr[n-1]
    j=j+1
    for i in range(0,j):
        arr[i] = res1[i]
    return j
arr = [1,1,2,3]
n = len(arr)
remove_Duplicate(arr,n)
for i in range(n):
    print(arr[i],end=' ')
