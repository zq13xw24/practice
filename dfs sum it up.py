n = int(input())
l = list(map(int, input().split(',')))
t = int(input())
ans = []
cnt = 0

def dfs(ai, bi, sum):
    if sum > t:
        return
    if sum == t:
        cnt = 1
        for i in range(bi+1):
            if i == bi:
                print("+%d", b[i])
