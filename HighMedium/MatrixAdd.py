
# Matrix addition
X = [[12,7,3],
    [4,5,6],
    [7,8,9]]
#    3X3
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
#    3X3
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
#         3X3
for i in range(len(X)):
     for j in range(len(X[0])):
          result[i][j]= X[i][j]+Y[i][j]

for r in result:
     print(r)

