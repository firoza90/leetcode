"""
https://leetcode.com/problems/binary-tree-paths/
Given the root of a binary tree, return all root-to-leaf paths in any order.
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""
from binary_tree import TreeNode, createTree
null = None

class Solution:
    def __init__(self):
        self.paths = []

    def _binaryTreePaths(self, root, path, length):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            self.paths.append('->'.join([str(p) for p in path]))
            return
        length = length+1
        self._binaryTreePaths(root.left, path, length)
        while len(path) > length:
            path.pop()
        self._binaryTreePaths(root.right, path, length)
        
    def binaryTreePaths(self, root):
        path = []
        self._binaryTreePaths(root, path, 0)
        return self.paths

    def test_binaryTreePaths(self):
        testcases = [[1,2,3,null,5],]
        for test in testcases:
            t = createTree(test)
            t.printTree()
            print(self.binaryTreePaths(t))