"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/ 
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
"""
from binary_tree import TreeNode, createTree
null = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def test_maxDepth(self):
        testcases = [[3,9,20,null,null,15,7],]
        for testcase in testcases:
            print(testcase)
            root = createTree(testcase)
            print(self.maxDepth(root))
