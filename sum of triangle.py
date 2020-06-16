'''
三角形至上而下的路径的最小和，只能走下一行相邻的
'''

n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split(','))))

for i in range(len(tri)-1, 0, -1):
    for j in range(i):
        tri[i-1][j] += min(tri[i][j], tri[i][j+1])
print(tri[0][0])