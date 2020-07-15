import sys

class Solution:
    def maxProfit(self, prices) -> int:
        min_, max_profit = sys.maxsize, 0

        for price in prices:
            if price < min_:
                min_ = price
            
            profit = price - min_
            if profit > max_profit:
                max_profit = profit

        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))