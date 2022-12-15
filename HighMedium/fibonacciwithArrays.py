# Fibonacci using array
# 0 1 1 2 3
import math
def isPerfectSquare(num):
    n = int(math.sqrt(num))
    return (n*n==num)
# check the values are fibonacci or not
def checkFib(array,n):
    count = 0
    for i in range(n):
        if (isPerfectSquare(5*array[i]*array[i]-4) or isPerfectSquare(5*array[i]*array[i]+4)):
            print(array[i]," ",end=" ")
            count = count+1
    if (count==0):
        print("None present")
array = [4,2,8,5,1,13,40,15]
n = len(array)
checkFib(array,n)





