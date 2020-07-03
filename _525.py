class Solution:
    def findMaxLength(self, nums) -> int:
        count = 0
        hashmap = {0 : 0}
        max_range = 0
        for i, num in enumerate(nums):

            if num == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap:
                max_range = max(max_range, i - hashmap[count])
            else:
                hashmap[count] = i

        return max_range
print(Solution().findMaxLength([0, 1]))