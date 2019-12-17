from unittest import TestCase

from _206 import *

head = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(None)

head.next = two
two.next = three
three.next = four
four.next = five
five.next = six

reverse_head = ListNode(None)
reverse_two = ListNode(5)
reverse_three = ListNode(4)
reverse_four = ListNode(3)
reverse_five = ListNode(2)
reverse_six = ListNode(1)

reverse_head.next = reverse_two
reverse_two.next = reverse_three
reverse_three.next = reverse_four
reverse_four.next = reverse_five
reverse_five.next = reverse_six


class TestSolution(TestCase):
    def test_reverseList(self):
        solution = Solution().reverseList(head)

        for i in range(5):
            solution_compare = solution
            reverse_compare = reverse_head

            for j in range(i):
                solution_compare = solution_compare.next
                reverse_compare = reverse_compare.next

            assert solution_compare.val == reverse_compare.val