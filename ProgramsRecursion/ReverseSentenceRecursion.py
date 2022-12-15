
n = 'rac'
print(n[::-1])

def recur_rev(n):
    if n == 1:
        return n
    else:
        return n[::-1]
print(recur_rev(n))
