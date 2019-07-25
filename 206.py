# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head.next
        previous = head

        while current:
            temp = ListNode(current.val)
            temp.next = previous
            
            previous = current
            current = current.next
            
        
        return temp  