"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given an array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
where 1 <= answer[0] < answer[1] <= numbers.length.
The tests are generated such that there is exactly one solution. 
You may not use the same element twice.
"""

class Solution:
    def twoSum(self, numbers, target):
        start, end = 0, len(numbers) - 1
        while start < end and end >= 0 and start < len(numbers):
            sum = numbers[start] + numbers[end]
            if sum == target:
                break
            if sum < target:
                start = start + 1
                continue
            if sum > target:
                end = end - 1
        return [start + 1, end + 1]

    def test(self):
        testcases = [([2,7,11,15], 9), ([2,3,4], 6), ([-1,0], -1)]
        for testcase in testcases:
            print(testcase)
            numbers, target = testcase
            result = self.twoSum(numbers, target)
            print(result)


def run():
    sol = Solution()
    sol.test()