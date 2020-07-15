
from functools import reduce

class Solution:
    def singleNumber(self, nums) -> int:
        return reduce((lambda x, y: x ^ y), nums)


print(Solution().singleNumber([2,2,1]))