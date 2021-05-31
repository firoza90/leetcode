
"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
from binary_tree import TreeNode, createTree
null = None

class Solution:
    def test_postorderTraversal(self):
        testCases = [[1,null,2,3], [], [1]]
        for testCase in testCases:
            print(testCase)
            tree = createTree(testCase)
            print(self.preorderTraversal(tree))
            print("\n\n")

    def postorderTraversal(self, root):
        if not root:
            return []
        result = []
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result
