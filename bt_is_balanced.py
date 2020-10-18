"""
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.
"""
from binary_tree import TreeNode, createTree
null = None

class Solution(object):
    def _isBalanced(self, root):
        if not root:
            return 0, True
        left_depth, left_balanced = self._isBalanced(root.left)
        right_depth, right_balanced = self._isBalanced(root.right)

        balanced = left_balanced and right_balanced and abs(left_depth-right_depth)in [0,1]
        depth = max(right_depth, left_depth)+1
        return depth, balanced

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, balanced = self._isBalanced(root)
        return balanced

root = createTree([1,2,3,4,5,6,null,8])
sol = Solution()
print(sol.isBalanced(root))
