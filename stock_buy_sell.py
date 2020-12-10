"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""

def maxProfit(prices):
    # 75% time efficiency, 35% space efficiency
    #minIndex, maxIndex = 0, 0
    #maxProfit = 0
    #for i in range(1, len(prices)):
    #    if prices[minIndex] >= prices[i]:
    #        minIndex = i
    #    if maxIndex <= minIndex:
    #       if prices[i] > prices[minIndex]:
    #           maxIndex = i
    #    else:
    #        if prices[maxIndex] <= prices[i]:
    #            maxIndex = i
    #    if minIndex < maxIndex:
    #        currProfit = prices[maxIndex] - prices[minIndex]
    #        if currProfit > maxProfit:
    #            maxProfit = currProfit
    #return maxProfit
    
    # 90% time efficiency, 80% space efficiency
    maxProfit = 0
    if len(prices) == 0:
        return 0
    minPrice = prices[0]
    for i in range(1, len(prices)):
        if minPrice > prices[i]:
            minPrice = prices[i]
        if maxProfit < prices[i] - minPrice:
            maxProfit = prices[i] - minPrice
    return maxProfit

testCases = [[7,1,5,3,6,4], [7,6,4,3,1], [], [-1]]
for testCase in testCases:
    print(testCase)
    print(maxProfit(testCase))
    print("\n\n")
