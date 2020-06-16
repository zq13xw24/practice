l = list(map(int, input().split(' ')))
n = l[0]
m = l[1]
k = l[2]
matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    matrix[0][i] = i+1
for i in range(n):
    matrix[i][0] = i+1
for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = matrix[0][j] * matrix[i][0]