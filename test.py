l = list(map(int, input().split()))
n = l[0]
m = l[1]
d = [0]
for i in range(m):
    d.append(int(input()))
p = d
max_d = sum(d)
target = max_d // 2 + 1
optp = [[0 for j in range(target+1)] for i in range(len(d))]
for i in range(1, len(p)):
    for j in range(1, target+1):
        if j >= p[i]:
            optp[i][j] = max(optp[i-1][j], optp[i-1][j-d[i]] + p[i])
        else:
            optp[i][j] = optp[i-1][j]
print(n-1-optp[-1][-1])