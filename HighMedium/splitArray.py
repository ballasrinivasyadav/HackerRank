
# Split the sorted array
# def splitArr(arr,n,k):
#     for i in range(0,k):
#         x=arr[0]
#         for j in range(0,n-1):
#             arr[j] = arr[j+1]
#         arr[n-1] = x
#
# arr = [2,10,5,6,52,36]
# n = len(arr)
# position = 2
# splitArr(arr,n,position)
# for i in range(0,n):
#     print(arr[i],end=' ')

#
# arr = [1,2,3,4,5]
# i=index = 2
# j=n = len(arr) = 5
# o/p:[3,4,5,1,2]

def splitArr(arr,n,index):
    for i in range(0,index): #0,1
        x = arr[0]           #1 #2
        for j in range(0,n-1): #0,1,2,3
            arr[j] = arr[j+1]  #1=2
        arr[n-1] = x
arr = [1,2,3,4,5]
index = 2
n = len(arr)
splitArr(arr,n,index)
for i in range(0,n):
    print(arr[i],end=' ')









