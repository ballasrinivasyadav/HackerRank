
def sum_recur(n):
    if n<=1:
        return n
    else:
        return n+sum_recur(n-1) # 16+15+14+13+12+11+10+9+8+7+6+5+4+3+2+1
n=16

print(sum_recur(n))
# if n<0:
#     print("the")
# else:
#     print(sum_recur(n))