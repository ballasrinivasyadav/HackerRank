
n = int(input("Enter:"))

def rec_fibonacci(first,second):

    for i in range(n):
        print(first,end='')
        temp = first
        first = second
        second = temp+first
rec_fibonacci(0,1)

