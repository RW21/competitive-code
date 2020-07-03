# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        min_ = -999999999999999
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= min_:
                return False
            min_ = root.val
            root = root.right
            
        return True



a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(4)
d = TreeNode(1)

a.left = b
b.left = d
a.right = c

s = Solution()
print(s.isValidBST(a))
