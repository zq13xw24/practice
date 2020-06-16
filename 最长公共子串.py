# s1 = [1,3,4,5,6,7,7,8]
# s2 = [3,5,7,4,8,6,7,8,2]

# dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
# max_l = 0
# p = 0
# for i in range(n):
#     for j in range(m):
#         if a[i] == b[j]:
#             dp[i+1][j+1] = dp[i][j]+1
#             if dp[i+1][j+1] > max_l:
#                 max_l = dp[i+1][j+1]
#                 p = i+1
# print(max_l)
# dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
# max_l = 0
# for i in range(1, len(s1)+1):
#     for j in range(1, len(s2)+1):
#         if s1[i-1] == s2[j-1]:
#             dp[i][j] = dp[i-1][j-1]+1
#             if dp[i][j] > max_l:
#                 max_l = dp[i][j]
# print(max_l)

# 最长公共子串
def longestCommonSubarray(s1, s2):
    if not s1 or not s2:
        return 0
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_l = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_l:
                    max_l = dp[i][j]
    return max_l

def longestCommonArray(s1, s2):
    if not s1 or not s2:
        return 0
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

if __name__ == "__main__":
    s1 = [1,3,4,5,6,7,7,8]
    s2 = [3,5,7,4,8,6,7,8,2]
    longSubarray = longestCommonSubarray(s1, s2)
    longCommonArray = longestCommonArray(s1, s2)
    print(longCommonArray)
    print(longSubarray)
