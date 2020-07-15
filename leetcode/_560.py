from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0, 0

        _map = {0: 1}

        for i in nums:
            sum += i
            if (sum - k) in _map:
                count += _map[sum - k]

            _map[sum] = _map.get(sum, 0) + 1

        return count


print(Solution().subarraySum([1, 1, 1], 2))