
# Smallest among N numbers in an array
N = 2
list1 = [1,2,10,25]
list1.sort()
print(list1[:N])

N=2 # i
arr = [1,20,55,100] #j
      #0 1 2 3
# O/P: 1,20
list2 = []
for i in range(N):
    min1 = 101
    for j in range(len(arr)):
        if arr[j]<min1:
            min1 = arr[j]
    arr.remove(min1)
    list2.append(min1)
print(list2)











# creating empty list
# list1 = []
# n = int(input("Enter Number of Elements in list:"))
# for i in range(n):
#     ele = int(input("Enter of elements"))
#     list1.append(ele)
# print("Smallest number from list:",min(list1))