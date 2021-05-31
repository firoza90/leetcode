"""
https://leetcode.com/problems/contains-duplicate-ii/
Given an integer array nums and an integer k, return true if
there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

class Solution:
    # O(kn) - slow 
    #def containsNearbyDuplicate(self, nums, k):
    #    for i in range(0, len(nums)):
    #        for j in range(i+1, i+k+1):
    #            if j >= len(nums):
    #                break
    #            if nums[i] == nums[j]:
    #                return True
    #    return False

    def containsNearbyDuplicate(self, nums, k):
        map = {}
        for index, num in enumerate(nums):
            i =  map.get(num, -1)
            if i != -1 and abs(index-i) <= k:
                return True
            map[num] = index
        return False

    def test_containsNearbyDuplicate(self):
        tests = [([1,2,3,1], 3), ([1,0,1,1], 1), ([1,2,3,1,2,3], 2)]
        for test in tests:
            print(test)
            print(self.containsNearbyDuplicate(test[0], test[1]))
