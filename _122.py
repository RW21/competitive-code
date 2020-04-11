'''
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        positive_depth = 0
        for i in range(len(prices)):
            if i + 1 != len(prices):
                positive = prices[i + 1] - prices[i]
                if positive > 0:
                    positive_depth += positive

        return positive_depth
