'''
xy迷宫里面最小的路径和
'''

n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(','))))

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = matrix[0][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1] + matrix[0][i]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
print(dp[-1][-1])