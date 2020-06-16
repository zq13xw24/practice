'''
最长公共子序列，子序列可以不是连续的。这个文件的名字错了，是longest common sequence
'''
s1 = [1,3,4,5,6,7,7,8]
s2 = [3,5,7,4,8,6,7,8,2]
# dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1) + 1)]
# for i in range(1, len(s1)+1):
#     for j in range(1, len(s2)+1):
#         if s1[i-1] == s2[j-1] and dp[i][j] < dp[i-1][j-1] + 1:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp[-1][-1])

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1] and dp[i][j] < dp[i-1][j-1] + 1:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])

