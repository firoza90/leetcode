"""
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

from binary_tree import TreeNode, createTree

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        right, left = root.right, root.left
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root

    def test_invertTree(self):
        testcases = [[4,2,7,1,3,6,9],]
        for testcase in testcases:
            print(testcase)
            root = createTree(testcase)
            self.invertTree(root).printTree()
