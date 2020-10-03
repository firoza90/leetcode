"""
https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

def threeSum(nums):
    results = []
    nums.sort()

    for i in range(0, len(nums) - 1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        low = i + 1
        high = len(nums) - 1
        while( low < high):
            sum = nums[i] + nums[low] + nums[high]
            if sum == 0:
                result = [nums[i], nums[low], nums[high]]
                results.append(result)
                low += 1
                high -= 1
                while (low < high and nums[low] == nums[low-1]):
                    low += 1
            elif sum < 0:
                low += 1
            else:
                high -= 1

    return results

print(threeSum([0,0,0,0,0,0,0]))
print(threeSum([-1,0,1,2,-1,-4]))