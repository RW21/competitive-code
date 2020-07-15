from unittest import TestCase
from _11 import Solution


class TestSolution(TestCase):
    def test_maxArea(self):
        assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
