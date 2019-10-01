# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False
            
            return True

        a = deque([(p,q)])

        while a:
            p, q = deque.popleft(a)
            
            if not check(p,q):
                return False
            
            if p:
                a.appendleft((p.left, q.left))
                a.appendleft((p.right, q.right))

        return True