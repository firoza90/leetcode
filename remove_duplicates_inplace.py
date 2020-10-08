"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    w_index, r_index = 0, 1

    while r_index < len(nums):
        if nums[w_index] == nums[r_index]:
            r_index += 1
        else:
            w_index += 1
            nums[w_index] = nums[r_index]
            r_index += 1

    return w_index + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
