from unittest import TestCase
from _104 import *


class TestSolution(TestCase):
    def test_maxDepth(self):
        root = TreeNode(3)
        root.right = TreeNode(9)
        root.left = TreeNode(20)
        root.left.left = TreeNode(15)
        root.left.right = TreeNode(7)

        assert Solution().maxDepth(root) == 3

