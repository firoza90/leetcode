"""
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        counter = 1
        candidateIndex = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[candidateIndex]:
                counter = counter + 1
            else:
                counter = counter - 1
            if counter < 0:
                candidateIndex = i
                counter = 1

        return nums[candidateIndex]

    def test(self):
        testcases = [[3,2,3], [2,2,1,1,1,2,2]]
        for testcase in testcases:
            print(testcase)
            print(self.majorityElement(testcase))