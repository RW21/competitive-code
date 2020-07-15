from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start = 0

        # find decreasing sublist
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                start = i

        # todo binary search to find num

        possibilities = sorted(nums[start - 1:len(nums)])
        replace_index = possibilities.index(nums[start - 1])
        possibilities.insert(0, possibilities[replace_index + 1])
        possibilities.pop(replace_index + 2)

        count = 0
        for i in range(start - 1, len(nums)):
            nums[i] = possibilities[count]
            count += 1

        print(possibilities)

Solution().nextPermutation([3,2,1])
