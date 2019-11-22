from unittest import TestCase
from _142 import Solution, ListNode


class TestSolution(TestCase):

    def test_142(self):
        node_with_loop = ListNode(3)
        a = ListNode(2)
        b = ListNode(0)
        c = ListNode(-4)

        node_with_loop.next = a
        a.next = b
        b.next = c
        c.next = b

        assert Solution().detectCycle(node_with_loop) == b

    def test_142_no_loop(self):
        node_with_no_loop = ListNode(3)
        a = ListNode(2)

        node_with_no_loop.next = a

        assert Solution().detectCycle(node_with_no_loop) is None

    def test_142_single_node_loop(self):
        a = ListNode(1)
        b = ListNode(2)
        a.next = a
        b.next = a

        assert Solution().detectCycle(a) == a
