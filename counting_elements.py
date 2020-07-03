from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        exists = set(arr)
        sum = 0
        for n in arr:
            if n + 1 in exists:
               sum += 1

        print(sum)
        return sum

Solution().countElements([1,1,2,2])

