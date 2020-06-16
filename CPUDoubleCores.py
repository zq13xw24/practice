'''
一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，假设已知CPU的每个核1秒可以处理1kb，
每个核同时只能处理一项任务。n个任务可以按照任意顺序放入CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，
求这个最小的时间。

输入包括两行：
第一行为整数n(1 ≤ n ≤ 50)
第二行为n个整数length[i](1024 ≤ length[i] ≤ 4194304)，表示每个任务的长度为length[i]kb，每个数均为1024的倍数。
输出一个整数，表示最少需要处理的时间。
问题实质是动态规划问题，把数组分成两部分，使得两部分的和相差最小。就是两个CPU各自处理的时间
'''

w = [0, 3072, 3072, 7168, 3072, 1024]     # 任务大小
w = list(map(lambda x: int(x/1024), w))
p = w       # 这题价值和任务重量一致
n = sum(w) / 2 + 1    # 背包承重为总任务的一半

optp = [[0 for j in range(n+1)] for i in range(len(w))]
for i in range(1, len(p)):
    for j in range(1, n+1):
        if j >= p[i]:
            optp[i][j] = max(optp[i-1][j], optp[i-1][j-w[i]] + p[i])
        else:
            optp[i][j] = optp[i-1][j]
print(optp[-1][-1])


