'''
求和为sum的方案数目
'''

num = 5
sum = 10
a = [5, 5, 10, 2, 3]

# 动态规划算法。dp[i][j]代表用前i个数字凑到j最多有多少种方案。
# dp[i][j]=dp[i-1][j];   //不用第i个数字能凑到j的最多情况
# dp[i][j]+=dp[i-1][j-value[i]];用了i时，只需要看原来凑到j-value[i]的最多情况即可。并累加
dp = [[1] + [0] * sum for _ in range(num+1)]
for i in range(1, num+1):
    for j in range(1, sum+1):
        if j - a[i-1] >= 0:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-a[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
