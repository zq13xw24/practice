'''
两个字符串，第一个最少经过多少次改变可以变成第二个单词，可以插入，改变，删除

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

'''

def minEditDis(s1, s2):
    if not s1 and not s2:
        return 0
    if len(s1) == 0 and len(s2) != 0:
        return len(s2)
    if len(s2) == 0 and len(s1) != 0:
        return len(s1)
    dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(len(s1)):
        dp[0][i] = i
    for j in range(len(s2)):
        dp[j][0] = j
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s1[i-1] == s2[i-1]:
                c = 0
            else:
                c = 1
            dp[i][j] = min(dp[i-1][j-1]+c, min(dp[i][j-1], dp[i-1][j])+1)
    return dp[-1][-1]
print(minEditDis("horse", "ros"))


