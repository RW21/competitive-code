import math
from typing import List


def majorityElement(nums: List[int]) -> int:
    majority = math.floor(len(nums) / 2)
    num_of = {}

    for num in nums:
        if num not in num_of:
            num_of[num] = 0
        else:
            num_of[num] += 1

        if num_of[num] >= majority:
            return num


print(majorityElement([3, 2, 3]))
