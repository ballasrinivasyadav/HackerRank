# Factors of a number


def factor(n):
    print("The factor number are:",n)
    for i in range(1,n+1):  # 1,5
        if n%i == 0:# 8%1 == 8  ok
                    # 8%2 == 4  ok
                    # 8%3 == 0
                    # 8%4 == 2  ok
                    # 8%5 == 0
                    # 8%6 == 0
                    # 8%7 == 0
                    # 8%8 == 1  ok
            print(i)
factor(8)

