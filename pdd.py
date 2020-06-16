l = input().split(';')
nums = l[0].split(',')
n = int(l[1])
nums = list(map(int, nums))
ans = []
nums.sort(reverse=True)
for i in nums:
    if i % 2 == 0:
        ans.append(i)
        if len(ans) == n:
            break
if len(ans) < n:
    for i in nums:
        if i % 2 != 0:
            ans.append(i)
            if len(ans) == n:
                break
print(",".join(str(i) for i in ans))
