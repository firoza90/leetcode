"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
"""

from binary_tree import TreeNode, createTree
null = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        level = []
        from collections import deque
        q = deque()
        q.append(root)
        q.append(None)
        while q:
            curr = q.popleft()
            if not curr:
                result.append(level)
                level = []
                if q:
                    q.append(None)
                    continue
                else:
                    break
            level.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return result[::-1]

root = createTree([3,9,20,1,null,15,7])
sol = Solution()
print(sol.levelOrderBottom(root))
