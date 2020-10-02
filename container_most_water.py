"""
https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
def maxArea(height):
    low, high = 0, len(height) - 1
    max_area = 0
    while (high - low >= 1 ):
        max_area = max(max_area, min(height[low], height[high]) * (high - low))
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    return max_area

print(maxArea([2,3,4,5,18,17,6]))
print(maxArea([1,8,6,2,5,4,8,3,7]))

