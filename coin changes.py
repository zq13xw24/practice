n = int(input())
values = list(map(int, input().split(' ')))
m = int(input())

dp = [float("inf")] * (m+1)
dp[0] = 0
for i in range(1, m+1):
    for value in values:
        if i - value >= 0:
            dp[i] = min(dp[i], dp[i - value] + 1)
if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])