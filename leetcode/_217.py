from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw = set()
        for num in nums:
            if num in saw:
                return True
            else:
                saw.add(num)

        return False
