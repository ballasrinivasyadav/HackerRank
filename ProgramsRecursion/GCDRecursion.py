# GCD using recursion
def gcd_recur(n, m):
    
    if (m == 0):
        return n
    else:
        return gcd_recur(m, n % m)


print(gcd_recur(64, 48))
