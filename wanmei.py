n = int(input())
m = int(input())
l = list(map(int, input().split(' ')))
if m == 0 or n == 0 or len(l) == 0:
    print(1)
matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = l[i*m+j]

dp = [[0] * m for _ in range(n)]
dp[n-1][m-1] = max(1-matrix[n-1][m-1] ,1)
for i in range(n-2, -1, -1):
    dp[i][m-1] = max(dp[i+1][m-1] - matrix[i][m-1], 1)
for j in range(m-2, -1, -1):
    dp[n-1][j] = max(dp[n-1][j+1] - matrix[n-1][j], 1)
for x in range(n-2, -1,-1):
    for y in range(m-2, -1, -1):
        dp[x][y] = max(min(dp[x+1][y] - matrix[x][y], dp[x][y+1] - matrix[x][y]) ,1)
print(dp[0][0])