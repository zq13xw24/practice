'''
房子圆形连接在一起的，意思是最后一个和第一个也是连接在一起的
'''

def HouseRobberII(house):
    if len(house) == 0:
        return 0
    if len(house) == 1:
        return house[0]
    if len(house) == 2:
        return max(house[0], house[1])
    def roober(start, stop, house):
        roob = house[start: stop+1]
        dp = [0] * len(roob)
        dp[0], dp[1] = roob[0], max(roob[0], roob[1])
        for i in range(2, len(roob)):
            dp[i] = max(dp[i-1], dp[i-2]+roob[i])
        return dp[-1]
    return max(roober(0, len(house)-2, house), roober(1, len(house)-1, house))

print(HouseRobberII([2,3,2]))