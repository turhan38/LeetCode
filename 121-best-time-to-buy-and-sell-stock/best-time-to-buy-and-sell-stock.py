class Solution(object):
    def maxProfit(self, prices):
        minV = float('inf') 
        maxV = 0
        for price in prices:
            if price < minV:
                minV = price
            elif price - minV > maxV:
                maxV = price - minV
        return maxV

        