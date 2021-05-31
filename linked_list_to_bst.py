"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
from binary_tree import TreeNode, createTree
null = None

class Solution(object):
    def _sortedArrayToBST(self, nums, low, high):
        if low > high :
            return None
        if low == high:
            return TreeNode(nums[low])
        mid = low + (high - low) // 2
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, low, mid-1)
        root.right = self._sortedArrayToBST(nums, mid+1, high)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._sortedArrayToBST(nums, 0, len(nums)-1)

    def test_sortedArrayToBST(self):
        self.sortedArrayToBST([-10,-3,0,5,9]).printTree()