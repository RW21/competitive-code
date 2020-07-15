class Solution:
    def reverse(self, x: int) -> int:


        ans = 0
        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10

        return ans


print(Solution().reverse(-32))
