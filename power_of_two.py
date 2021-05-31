"""
https://leetcode.com/problems/power-of-two/
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n and not (n & (n-1)))


    def test_isPowerOfTwo(self):
        tests = [2147483647, 1073741824, -2147483648, 1, 2, 3, -2, -4, -1, -2147483646, -16]
        for test in tests:
            print(test)
            print(self.isPowerOfTwo(test))