
# Linear Search
def linearSearch(array,n,x):
    # Going through array sequential
    for i in range(0,n):
        if (array[i]== x):
            return i
    return -1

array = [2,4,0,3,1]
x=1
n=len(array)
result = linearSearch(array,n,x) #  5 , 1
if(result == -1):
    print("Element not found")
else:
    print("element found at index",result)