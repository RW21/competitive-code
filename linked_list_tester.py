class ListNode:
    def __init__(self, x):
        if type(x) == list:
            x: list
            x.reverse()
            node = ListNode(x.pop())
            head = node

            try:
                while a := x.pop():
                    node.next = ListNode(a)
                    node = node.next
            except IndexError:
                self.val = head.val
                self.next = head.next
        else:
            self.val = x
            self.next = None

    def __str__(self):
        string = ''
        node = self
        while node is not None:
            if node.next is None:
                arrow = ''
            else:
                arrow = ' -> '
            string += str(node.val) + arrow
            node = node.next

        return string