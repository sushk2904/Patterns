matrix = [[5,10,8], [7,6,3], [2,1,9]]

rows = len(matrix)
cols = len(matrix[0])
for i in range(0,rows):
    for j in range(0, cols):
        print(matrix[i][j], end= " ")
    print()


n = len(matrix)
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
    matrix[i].reverse()

rows1 = len(matrix)
cols1 = len(matrix[0])
for i in range(0,rows1):
    for j in range(0, cols1):
        print(matrix[i][j], end= " ")
    print()