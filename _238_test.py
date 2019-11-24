from unittest import TestCase
from _238 import Solution


class TestSolution(TestCase):
    def test_productExceptSelf(self):
        assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_productExceptSelf_2(self):
        assert Solution().productExceptSelf([4, 5, 1, 8, 2]) == [80, 64, 320, 40, 160]
