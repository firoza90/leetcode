"""
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        read, write = 0, 0
        for read in range(0, len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write = write + 1
        for i in range(write, len(nums)):
            nums[i] = 0

    def test_moveZeroes(self):
        testcases = [[0,1,0,3,12], [0]]
        for testcase in  testcases:
            print(testcase)
            self.moveZeroes(testcase)
            print(testcase)

        
