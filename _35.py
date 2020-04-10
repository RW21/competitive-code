from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    # edge cases
    if target <= nums[0]:
        return 0

    if target == nums[len(nums) - 1]:
        return len(nums) - 1
    if target > nums[len(nums) - 1]:
        return len(nums)

    for i, num in enumerate(nums):
        if i != len(nums) - 1:
            if num == target:
                return i
            if num < target < nums[i + 1]:
                return i + 1


print(searchInsert([1, 3], 3))
