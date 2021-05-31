"""
https://leetcode.com/problems/path-sum/
Given a binary tree and a sum, 
determine if the tree has a root-to-leaf path such that 
adding up all the values along the path equals the given sum.
"""
from binary_tree import TreeNode, createTree
null = None

class Solution:
    def _hasPathSum(self, root, sum, reqSum):
        sum += root.val
        if not root.left and not root.right:
            return (sum == reqSum)
        if root.left:
            if self._hasPathSum(root.left, sum, reqSum):
                return True
        if root.right:
            if self._hasPathSum(root.right, sum, reqSum):
                return True
        return False

    def hasPathSum(self, root, sum):
        if not root:
            return False
        return self._hasPathSum(root, 0, sum)

    def test_hasPathSum(self):
        testcases = [([5,4,8,11,null,13,4,7,2,null,null,null,1], 22), ([1,2], 1), ([], 0)]
        for testcase in testcases:
            print(testcase)
            treeValue, sum = testCase
            tree = createTree(treeValue)
            result = self.hasPathSum(tree, sum)
            tree.printTree() if tree else print("[]")
            print(sum)
            print("Result : %s\n\n" %result)
