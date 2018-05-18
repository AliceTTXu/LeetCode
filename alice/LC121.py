class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        max_profit = 0
        current_min = prices[0]
        
        for price in prices:
            if price < current_min:
                current_min = price
            else:
                max_profit = max(max_profit, price - current_min)
                
        return max_profit