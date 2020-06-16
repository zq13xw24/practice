n = int(input())
t = input()
m = int(input())
ans = 0
for i in range(m):
    s = input()
    x = 0
    j = 0
    while j < n:
        if t[j] == s[x]:
            x += 1
            j += 1
            if x == len(s):
                x = 0
        else:
            break
    if j == n:
        ans += 1
print(ans)