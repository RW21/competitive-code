from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        q = deque()
        q.append(root)

        while len(q) != 0:
            current = q.pop()
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left is not None:
                q.append(current.left)

            if current.right is not None:
                q.append(current.right)

        return root
