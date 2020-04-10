class Solution:
    def romanToInt(self, s: str) -> int:
        nums = []
        for c in s:
            if c == 'I':
                nums.append(1)
            if c == 'V':
                nums.append(5)
            if c == 'X':
                nums.append(10)
            if c == 'L':
                nums.append(50)
            if c == 'C':
                nums.append(100)
            if c == 'D':
                nums.append(500)
            if c == 'M':
                nums.append(1000)

        to_int = 0

        for i in range(len(nums)):
            if i + 1 == len(nums):
                to_int += nums[i]

                break

            if nums[i] < nums[i + 1]:
                to_int -= nums[i]
            else:
                to_int += nums[i]

        return to_int


a = Solution()
print(a.romanToInt('XLIX'))
