"""
https://leetcode.com/problems/summary-ranges/
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

class Solution:
    def summaryRanges(self, nums):
        result = []
        if not nums:
            return result
        start_range = nums[0]
        end_range = None
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                end_range = nums[i]
            else:
                result.append("%d->%d" %(start_range, end_range) if end_range else str(start_range))
                start_range = nums[i]
                end_range = None
        result.append("%d->%d" %(start_range, end_range) if end_range else str(start_range))
        return result

    def test_summaryRanges(self):
        testcases = [[0,1,2,4,5,7], [0,2,3,4,6,8,9], [], [-1], [0]]
        for test in testcases:
            print(test)
            print(self.summaryRanges(test))


        