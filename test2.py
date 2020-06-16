import math
pic = list(map(int, input().split()))
h = pic[0]
w = pic[1]
cell = []
for i in range(h):
    cell.append(list(map(int, input().split())))
size = int(input())
core = []
for i in range(size):
    core.append(list(map(float, input().split())))
core_new = []
for i in range(size):
    for j in range(size):
        core_new.append(core[i][j])
res = []
tmp = []
for i in range(h-size+1):
    for j in range(w-size+1):
        for x in range(size):
            for y in range(size):
                tmp.append(cell[i+x][j+y])
for i in range(0,len(tmp), size+size):
    t = tmp[i:i+size+size]
    _ = list(map(lambda x,y: x*y, t, core_new))
    res.append(math.floor(sum(_)))
# for i in range(0,size):
#     print(''.join(str(res[i])))



# 3 3
# 40 24 135
# 200 239 238
# 90 34 94
# 2
# 0.0 0.6
# 0.1 0.3