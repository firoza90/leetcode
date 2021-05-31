"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

class Solution:
    # Runtime: 64 ms, faster than 40.44% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    # Memory Usage: 15.1 MB, less than 63.42% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    #def maxProfit(self, prices):
    #    min, max = 0, -1
    #    currProfit, totalProfit = 0, 0
    #    for i in range(1,len(prices)):
    #        if max > min and prices[i] < prices[max]:
    #            totalProfit = totalProfit + currProfit
    #            currProfit = 0
    #            max = -1
    #            min = i
    #        if prices[i] < prices[min]:
    #            min = i
    #        if (max == -1 or prices[max] <= prices[i]) and prices[min] < prices[i]:
    #            max = i
    #            currProfit = prices[max] - prices[min]
    #    if max == len(prices)-1:
    #        totalProfit = totalProfit + prices[max] - prices[min]
    #    return totalProfit


    def maxProfit(self, prices):
        maxProfit = 0
        low, high = prices[0], prices[0]
        i = 0
        while i < len(prices) -1 :
            while (i < len(prices) - 2) and prices[i] >= prices[i+1]:
                i = i+1
            low = i
            i = i+1
            while (i < len(prices) - 2) and prices[i] <= prices[i+1]:
                i = i+1
            high = i
            maxProfit = maxProfit + prices[high] - prices[low]
        return maxProfit

    def test_maxProfit(self):
        testCases = [[1,9,6,9,1,7,1,1,5,9,9,9], [2,4,1], [7,1,5,3,6,4], [1,2,3,4,5]]
        for testCase in testCases:
            print(testCase)
            print(self.maxProfit(testCase))
            print("\n\n")

        