n = int(input())
touzi = list(map(int, input().split(' ')))
min_v = min(touzi)
max_v = max(touzi)
ans = float(0)

def cal_C(n,m):
    fenzi = 1
    fenmu = 1
    for i in range(m, m-n+1, -1):
        fenzi *= i
    for i in range(n, 0, -1):
        fenmu *= i
    return float(fenzi/fenmu)

if __name__ == "__main__":
    for i in range(1, min_v + 1):
        ans += float((1 / min_v)**2) * i
        if i > 1:
            for j in range(1, n):
                ans += cal_C(j, i) * float((1 / min_v)) * i


