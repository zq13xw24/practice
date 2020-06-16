n = int(input())
value = list(map(int, input().split(' ')))
m = int(input())

dp = [[float("inf") for _ in range(m+1)] for _ in range(n)]
dp[0][0] = 0
for i in range(1, m+1):
    if i - value[0] >= 0:
        dp[0][i] = dp[0][i-value[0]] + 1
for i in range(1, n):
    for j in range(1, m+1):
        if j - value[i] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-value[i]] + 1)
if dp[-1][-1] == float("inf"):
    print(-1)
else:
    print(dp[-1][-1])
print(dp)

