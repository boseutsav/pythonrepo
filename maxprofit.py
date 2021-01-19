def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = sell = 0
    bf = sf = 0
    profit = 0
    for each in range(len(prices) - 1):
        if prices[each] < prices[each + 1] and bf == 0:
            buy = prices[each]
            bf=1
        elif prices[each] > prices[each + 1] and sf == 0 and bf != 0:
            sell = prices[each]
            sf=1
        if each == len(prices) - 2 and bf != 0 and sf == 0:
            sell = prices[each + 1]
            sf = 1
        if bf != 0 and sf != 0:
            profit += sell - buy
            buy = sell = 0
            bf= sf = 0
    return profit

print(maxProfit([2,1,2,0,1]))