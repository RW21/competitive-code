<<<<<<< HEAD
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(n -1 ):
            a, b = b, a+b
        return a
=======
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(n -1 ):
            a, b = b, a+b
        return a

print(Solution().climbStairs(500))
>>>>>>> 88312a6e16212060ee3c045a2612f2aef97eaf58
