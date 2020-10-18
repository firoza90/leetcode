"""
https://leetcode.com/problems/merge-sorted-array/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
"""

def merge(nums1, m, nums2, n):
    if m == 0:
        for i in range(0, n):
            nums1[i] = nums2[i]
        return nums1
    if n == 0:
        return nums1
    i = len(nums1) - 1
    m-=1
    n-=1

    while i >= 0 and m >= 0 and n >= 0:
        if nums2[n] > nums1[m]:
            nums1[i] = nums2[n]
            n-=1
        else:
            nums1[i] = nums1[m]
            m-=1
        i-=1

    if n >= 0:
        for i in range(0, n+1):
            nums1[i] = nums2[i]

    return nums1


print(merge([0], 0, [1], 1))

