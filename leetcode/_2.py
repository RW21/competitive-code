# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack = []
        end1, end2 = False, False

        while True:
            stack.append(l1.val + l2.val)

            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
                end1 = True

            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0
                end2 = True

            if end1 and end2:
                break

        num = ListNode
        # stack = [7, 10, 7 ,1]
        for i, n in enumerate((stack)):
            if n >= 10:
                if i == 0:
                    num += (n - 10)
                else:
                    num += (n - 10) * 10 ** i
                num += 10 ** (i + 1)
            else:
                if i == 0:
                    num += n
                else:
                    num += (n) * 10 ** i

        return num


a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)

print(Solution().addTwoNumbers(a, b))
