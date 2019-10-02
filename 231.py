class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        #
        # if n == 0:
        #     return False
        #
        # while n % 2 == 0:
        #     n /= 2
        #     if n == 1:
        #         return True
        #
        # return False
        return n > 0 and not (n & n - 1)


a = Solution()
print(a.isPowerOfTwo(63))
