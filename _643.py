"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        from collections import deque
        
        nums_for_average = deque([])

        for i, a in enumerate(nums):
            if i < k:
                nums_for_average.append(a)
                
            else:
                average = sum(nums_for_average) / k
                if average < a:
                    nums_for_average.popleft()
                    nums_for_average.append(a)
        return average
                
                
        