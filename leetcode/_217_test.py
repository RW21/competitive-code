from unittest import TestCase
from _217 import Solution


class TestSolution(TestCase):
    def test_containsDuplicate(self):
        assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

    def test_does_not_contain_duplicate(self):
        assert not Solution().containsDuplicate([1, 2, 3, 4])
