t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    max_v = 0
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for j in dic:
        max_v = max(dic[j], max_v)
    if max_v > (n / 2):
        print('NO')
    else:
        print('YES')