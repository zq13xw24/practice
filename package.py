'''
背包问题
'''

w = [0, 1, 4, 3, 1]    # 每个物体的重量wi，w0无用
p = [0, 1500, 3000, 2000, 2000]    # 每个物体的价值
n = len(w) - 1    # 物体的个数
m = 4     # 背包的载重

x = []   # 装入背包的物体，元素为true时，对应物体被装入，x0无用
v = 0
# optp[i][j]表示前i个物体中，能装进载重量为j的背包中的物体最大价值
optp = [[0 for col in range(m+1)] for raw in range(n+1)]   # n行m列

def packageDP(w, p, m, x):
    # 计算optp[i][j]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j >= w[i]:
                optp[i][j] = max(optp[i-1][j], optp[i-1][j-w[i]] + p[i])   # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
                # 这里的意思是在选第n行的时候，在重量等于j的时候，看是维持上一行的时候价值大还是选择这一行的价值大。
            else:
                optp[i][j] = optp[i-1][j]

    # 递推装入背包的物体，寻找跳变的地方，从最后结果开始逆推
    j = m
    for i in range(m, 0, -1):
        if optp[i][j] > optp[i-1][j]:
            x.append(i)
            j = j - w[i]
    # 返回最大值，即表格中最后一行最后一列的值
    v = optp[n][m]
    print(optp)
    return v

packageDP(w, p, m, x)
