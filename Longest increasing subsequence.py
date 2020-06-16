'''
给一个长度为N的序列，求出最长非降序列的长度
'''

lis = [2, 1, 5, 3, 6, 4, 8, 9, 7]
ans = 0
def longestIncreasingSubsequence(lis):
    dp = [1 for _ in range(len(lis))]
    res = 1
    for i in range(len(lis)):
        for j in range(i):
            if lis[j] < lis[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
            if dp[j] > res:
                res = dp[j]
    print(res)

# '''
# 求这个最长非减序列的和
# '''
# def longestIncreasingSubsequenceSum(lis):
#     dp = [[0 for i in range(2)] for i in range(len(lis))]
#     dp[0][0] = 0
#     dp[0][1] = lis[0]
#     for i in range(len(lis)):
#         for j in range(i):
#             if lis[j] <= lis[i] and dp[i][:] < dp[j][:] + 1:
#                 dp[i][:] = dp[j][:] + 1
#                 dp[i][0] = dp[j][1]
#                 dp[i][1] = dp[j][1] + lis[j]
#     print(dp[-1][-1])
# longestIncreasingSubsequenceSum(lis)
#


