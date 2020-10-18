"""
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()

            if left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            elif not left and not right:
                continue
            else:
                return False
        return True


