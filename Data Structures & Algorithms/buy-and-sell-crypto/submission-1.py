class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        currmin = prices[0]

        for i in range(len(prices) - 1):
            if prices[i] < currmin:
                currmin = prices[i]

            if prices[i+1] - currmin > maxprofit:
                maxprofit = prices[i+1] - currmin
        
        return maxprofit

            

            


            


        