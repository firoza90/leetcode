"""
https://leetcode.com/problems/find-duplicate-subtrees/
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
"""

from binary_tree import TreeNode, createTree
null = None

class Solution:
    def findDuplicateSubtrees(self, root):
        def traverse(root):
            if not root:
                return "null"
            struct = "%s,%s,%s" %(root.val, traverse(root.left), traverse(root.right))
            nodes.setdefault(struct, []).append(root)
            return struct

        nodes = {}
        traverse(root)
        result = [nodes[s][0] for s in nodes if len(nodes[s]) > 1]
        return result

    def test_findDuplicateSubtrees(self):
        testcases = [ [1,2,3,4,null,2,4,null,null,4], [2,1,1]]
        for testcase in testcases:
            print(testcase)
            tree = createTree(testcase)
            nodes = self.findDuplicateSubtrees(tree)
            print([node.val for node in nodes])
