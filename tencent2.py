l = list(map(int, input().split()))
n = l[0]
p = l[1]
q = l[2]

def cal_C(n,m):
    fenzi = 1
    fenmu = 1
    for i in range(m, m-n, -1):
        fenzi *= i
    for i in range(1, n+1):
        fenmu *= i
    return int(fenzi/fenmu)

if __name__ == "__main__":
    fenzi = 0
    fenmu = 0
    ans = 0
    for i in range(p, n-q+1):
        fenmu += cal_C(i, n)
    for i in range(p, n-q+1):
        fenzi = cal_C(i, n)
        ans += fenzi  * i
    print((ans+100000007)/fenmu)