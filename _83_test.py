from unittest import TestCase
from _83 import *


class TestSolution(TestCase):

    def test_deleteDuplicates(self):
        list_with_duplicate = ListNode(1)
        list_with_duplicate.next = ListNode(1)
        list_with_duplicate.next.next = ListNode(2)

        solution = Solution().deleteDuplicates(list_with_duplicate)

        list_with_duplicate.next = ListNode(2)

        assert solution.val == 1
        assert solution.next.val == 2
