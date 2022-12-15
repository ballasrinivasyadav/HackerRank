
# Sum of array using pointers
arr = [10,25,15,35,5,20]
def sumOfarray(arr):
    return sum(arr)
print(sumOfarray(arr))


def indices_sum(number,targets):
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i]+number[j] == targets:
                return(i,j)
number=[2,3]
targets = 5
print(indices_sum(number,targets))