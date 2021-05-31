"""
https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,1]
Output: 1
"""

class Solution:
    def singleNumber(self, nums):
        result = 0
        for item in nums:
            result = result ^ item
        return result

    def test_singleNumber(self):
        testCases = [[2,2,1],  [4,1,2,1,2], [1]]
        for testCase in testCases:
            print(testCase)
            print(self.singleNumber(testCase))
            print("\n\n")
