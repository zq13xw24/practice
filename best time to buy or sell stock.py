'''
只有一次机会买卖
'''
def maxProfit(stock):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(stock)):
        min_price = min(min_price, stock[i])
        max_profit = max(max_profit, stock[i]-min_price)
    return max_profit

def maxProfitII(stock):
    max_sofar = max_cur = 0
    for i in range(len(stock) - 1):
        max_cur = max(0, max_cur + stock[i+1] - stock[i])
        max_sofar = max(max_cur, max_sofar)
    return max_sofar

def maxProfitDP(stock):
    if not stock:
        return 0
    dp = [0] * len(stock)
    min_price = stock[0]
    for i in range(1, len(stock)):
        dp[i] = max(dp[i-1], stock[i]-min_price)
        if stock[i] < min_price:
            min_price = stock[i]
    return dp[-1]

'''
可以进行多次购买，同一天可以进行同时买卖，只要有正向序列就可以
'''

def maxProfitMul(stock):
    max_profit = 0
    for i in range(len(stock)-1):
        if stock[i+1] > stock[i]:
            max_profit += stock[i+1] - stock[i]
    return max_profit


'''
只能进行2次购买
'''
def maxProfitTwi(stock):
    if not stock:
        return 0
    max_sofar = [0] * 3
    max_cur = [0] * 3
    for i in range(1, len(stock)):
        diff = stock[i] - stock[i-1]
        for j in range(2, 0, -1):
            max_cur[j] = max(max_sofar[j-1] + max(diff, 0), max_cur[j] + diff)
            max_sofar[j] = max(max_sofar[j], max_cur[j])
    return max_sofar[-1]

def maxProfitTwiII(stock):
    if not stock:
        return 0
    dp1 = [0] * len(stock)
    dp2 = [0] * len(stock)
    # 在i之前进行交易获得的最大利润
    min_price = stock[0]
    for i in range(1, len(stock)):
        dp1[i] = max(dp1[i-1], stock[i] - min_price)
        min_price = min(stock[i], min_price)
    # 在i之后进行交易获得的最大利润
    max_price = stock[-1]
    for i in range(len(stock)-2, -1, -1):
        dp2[i] = max(dp2[i+1], max_price-stock[i])
        max_price = max(max_price, stock[i])

    max_profit = 0
    for i in range(len(stock)):
        if dp1[i] + dp2[i] > max_profit:
            max_profit = dp1[i] + dp2[i]
    return max_profit

'''
可以多次交易，但是卖出去之后要冷静1天，再进行购买
'''
def maxProfitCool(stock):
    if not stock:
        return 0
    sell = [0] * len(stock)    # sell[i]是第i天手里没股票的最大利润，今天卖了股票或者没动作
    hold = [0] * len(stock)    # hold[i]是第i天手里有股票的最大利润，今天买了股票或者没动作
    hold[0] = -stock[0]
    for i in range(1, len(stock)):
        sell[i] = max(sell[i-1], hold[i-1] + stock[i])
        hold[i] = max(hold[i-1], sell[i-2] - stock[i])
    return sell[-1]     # 最后一定是要手里没有股票

'''
每次都有手续费
'''
def maxProfiFee(stock, fee):
    if not stock:
        return 0
    sell = [0] * len(stock)
    hold = [0] * len(stock)
    hold[0] = -stock[0]
    for i in range(len(stock)):
        sell[i] = max(sell[i-1], hold[i-1] + stock[i] - fee)
        hold[i] = max(hold[i-1], sell[i-1] - stock[i] - fee)
    return sell[-1]
