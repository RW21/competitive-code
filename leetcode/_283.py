from typing import List

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)):
            if nums[i] == 0 and index == -1:
                index = i
            else:
                if index != -1 and nums[i] != 0:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1


        print(nums)


print(Solution().moveZeroes([1, 0, 1]))