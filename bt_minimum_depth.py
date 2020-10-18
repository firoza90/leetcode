"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes alo
ng the shortest path from the root node down to the nearest leaf node.
"""
from binary_tree import TreeNode, createTree
null = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else: 
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 


root = createTree([3,9,20,null,null,15,7])
sol = Solution()
print(sol.minDepth(root))