
# Transpose of a matrix
x = [[12,7],
     [4,5],
     [3,8]]
# Expected Output

result = [[0,0,0],
          [0,0,0]]

for i in range(len(x)):   #3
    for j in range(len(x[0])):#2
        result[j][i] = x[i][j]
for r in result:
    print(r)

print(len(x))
print(len(x[0]))
print(x[i])
print(result[j])

# Other Way
p = int(input("Enter the number of rows:"))
q = int(input("Enter the number of columns:"))

print("Enter the elements for matrix:")
matrix1 = [[int(input()) for i in range(q)] for j in range(p)]
print("matrix")
for i in range(p):
    for j in range(q):
        print(format(matrix1[i][j],"<4"),end="")
    print()


result = [[0 for i in range(p)] for j in range(q)]
for i in range(q):
    for j in range(p):
        result[i][j] = matrix1[j][i]
print("result")
for i in range(q):
    for j in range(p):
        print(format(result[i][j],"<4"),end="")
    print()

