

#Pascal triangle

n = int(input("Enter numbers:"))
list1 = []
for row in range(n):
    temp_list = []
    for col in range(row+1):
        if col == 0 or col == row:
            temp_list.append(1)
        else:

            temp_list.append(list1[row-1][col-1]+list1[row-1][col])
    list1.append(temp_list)
    print(list1)

for row in range(n):
    for col in range(n-row-1):
        print(" ",end="")
    for col in range(row+1):
        print(list1[row][col],end=" ")
    print()












