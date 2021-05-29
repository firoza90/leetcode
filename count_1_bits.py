"""
https://leetcode.com/problems/number-of-1-bits/
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 2**31
        count = 0
        for i in range(32):
            if mask & n:
                count = count + 1
            mask = mask >> 1
        return count

    def test(self):
        testcases = [0b00000000000000000000000000001011, 0b00000000000000000000000010000000, 0b11111111111111111111111111111101, ]
        for testcase in testcases:
            print(testcase)
            print(self.hammingWeight(testcase))
            print("")
