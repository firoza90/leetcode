"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
"""

def maxSubArray(nums):
    max_sum, curr_sum = -float("inf"), 0

    for i in range(0, len(nums)):
        curr_sum += nums[i]
        if curr_sum >= max_sum:
            max_sum = curr_sum
        if curr_sum <= 0:
            curr_sum = 0
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

