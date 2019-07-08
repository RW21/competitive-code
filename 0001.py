"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_sum = {}
        mapping = {}

        for index, i in enumerate(nums):
            diff = target - i
            
            if checked_sum.get(i) == diff:
                return [mapping[checked_sum[i]], index]
            
            checked_sum[diff] = i
            mapping[i] = index
            
            
        
            
            
        