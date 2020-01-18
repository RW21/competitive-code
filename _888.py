from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum1, sum2 = sum(A), sum(B)
        B = set(B)
        for one in A:
            temp = int((sum2 + 2 * one - sum1) / 2)
            if temp in B:
                return [one, temp]
