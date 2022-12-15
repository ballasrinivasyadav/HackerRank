# Expected Output : 5*4*3*2 = 120


def recursive_(n):
    if n == 1:
        return n
    else:
        return n*recursive_(n-1)
n = 5
if n>0:
    print(n,"is",recursive_(n))
