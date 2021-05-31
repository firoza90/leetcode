"""
https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
Input: nums = [1,3,5,6], target = 5
Output: 2   
"""

class Solution:
    def searchInsert(self, nums, target):
        #handle empty list
        if not nums:
            return 0

        if nums[0] == target:
            return 0

        if nums[-1] == target:
            return len(nums) - 1

        #handle edge cases
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def test_searchInsert(self):
        print(self.searchInsert([1,2,3,4,5,10], 2))

