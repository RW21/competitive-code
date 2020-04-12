# Definition for singly-linked list.
from linked_list_tester import ListNode
'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        if head.next is None:
            return head
        if head.next.next is None:
            return head.next

        while fast.next is not None:
            slow = slow.next

            if fast.next.next is None:
                fast = fast.next
            else:
                fast = fast.next.next

        return slow

print(Solution().middleNode(ListNode([1,2,3,4,5])))