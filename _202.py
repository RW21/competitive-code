class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            return sum([int(a) ** 2 for a in str(n)])

        slow, fast = n, next(n)

        while slow != fast and fast != 1:
            slow = next(slow)
            fast = next(next(fast))

        return slow != fast or fast == 1

Solution().isHappy(2)