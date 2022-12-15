# Largest among N numbers in an array
# element from given list of integers
# Function return N the largest elements
# N=2
# array = [1,2,10,15]
# array.sort()
# print(array[N:])

arr = [1,2,3,4,5]
      #0 1 2 3 4
N = 2
#output = 4,5

emp_list1 = []
for i in range(N):
    max1 = 0
    for j in range(len(arr)):
        if arr[j]>max1:
            max1 = arr[j]
    arr.remove(max1)
    emp_list1.append(max1)
print(emp_list1)








def Nmaxelements(list1,N):
    final_list = []
    for i in range(0,N):
        max1 = 0
        for j in range(len(list1)): # 4,3,2,1,0
            if list1[j] > max1:     # list1[4,3,2,1,0] > 0 : True
                max1 = list1[j]     # 0 = list1[4,3,2,1,0]
        list1.remove(max1)
        final_list.append(max1)     #
    print(final_list)
# Driver Code
list1 = [1,2,10,15,18]
N = 2
Nmaxelements(list1,N)




















