"""
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expectedSum = int((n * (n+1))/2)
        givenSum = sum(nums)
        return (expectedSum-givenSum)
    
    def test_missingNumber(self):
        testcases = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1],  [0], ]
        for testcase in testcases:
            print(testcase)
            print(self.missingNumber(testcase))
        