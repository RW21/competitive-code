from data_structures import TreeNode


class Solution():
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def traverse(node):
            if not node:
                return 0

            left, right = traverse(node.left), traverse(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        traverse(root)
        return self.diameter

t = TreeNode([1, 2, 3, 4])
print(Solution().diameterOfBinaryTree(t))
