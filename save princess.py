'''
迷宫救公主最少需要多少血
'''

n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(' '))))
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[-1][-1] = max(1, 1-matrix[-1][-1])
for i in range(n-2, -1, -1):
    dp[i][m-1] = max(dp[i+1][m-1]-matrix[i][m-1], 1)
for i in range(m-2, -1, -1):
    dp[n-1][i] = max(dp[n-1][i+1]-matrix[n-1][i], 1)
for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        dp[i][j] = max(min(dp[i+1][j]-matrix[i][j], dp[i][j+1]-matrix[i][j]), 1)
print(dp[0][0])
