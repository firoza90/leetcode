"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
from binary_tree import TreeNode, createTree
null = None


class Solution:
    def test_preorderTraversal(self):
        testCases = [[1,null,2,3], [], [1]]
        for testCase in testCases:
            print(testCase)
            tree = createTree(testCase)
            print(self.preorderTraversal(tree))
            print("\n\n")

    def preorderTraversal(self, root):
        if not root:
            return []
        result = []
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result
