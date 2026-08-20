class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left = 0

        for i in range(0,len(prices)):
            if prices[left] > prices[i]:
                left = i
            if prices[i] > prices[left]:
                diff = prices[i] - prices[left]
                maxprofit = max(diff , maxprofit)
        return maxprofit

        