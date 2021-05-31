"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
"""
from binary_tree import TreeNode, createTree
null = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if (root.val <= p.val and root.val >= q.val)  or (root.val >= p.val and root.val <= q.val):
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

    def test_lowestCommonAncestor(self):
        tests = [( [6,2,8,0,4,7,9,null,null,3,5], 2, 8), ([6,2,8,0,4,7,9,null,null,3,5], 2, 4), ([2,1], 2,1)]
        for test in tests:
            tree, p, q = test
            tree = createTree(tree)
            tree.printTree()
            p = TreeNode(p)
            q = TreeNode(q)
            lca = self.lowestCommonAncestor(tree, p, q)
            if lca:
                print(lca.val)
            else:
                print("no lca")
        
