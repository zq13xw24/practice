'''
有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同。参与挖矿工人的总数是10人。每座金矿要么全挖，
要么不挖，不能派出一半人挖取一半金矿。要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？
'''

n = int(input())
m = int(input())
situation = []
for i in range(n):
    situation.append(list(map(int, input().split())))

dp = [[0 for _ in range(m+1)] for i in range(n)]
dp[0][0] = 0
for i in range(m+1):
    if i >= situation[0][1]:
        dp[0][i] = situation[0][0]
for i in range(1, n):
    for j in range(m+1):
        if j >= situation[i][1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-situation[i][1]]+situation[i][0])
        else:
            dp[i][j] = dp[i-1][j]
print(dp)