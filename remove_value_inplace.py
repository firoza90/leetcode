
"""
https://leetcode.com/problems/remove-element/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    def removeElement( self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        w_index = 0

        for r_index in range(0, len(nums)):
            if val != nums[r_index]:
                nums[w_index] = nums[r_index]
                w_index += 1
        return w_index

    def test_removeElement(self):
        print(self.removeElement([0,1,2,2,3,0,4,2],2))