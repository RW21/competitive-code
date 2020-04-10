from unittest import TestCase
from _49 import *


class TestSolution(TestCase):
    def test_groupAnagrams(self):
        assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'],
                                                                                        ['tan', 'nat'], ['bat']]
