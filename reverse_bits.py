"""
https://leetcode.com/problems/reverse-bits/
Reverse bits of a given 32 bits unsigned integer.
Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
"""

class Solution:
    # slower
    #def reverseBits(self, n: int) -> int:
    #    binary = [0] * 32
    #    index = 0
    #    while n > 0:
    #        remainder = n % 2
    #        binary[index] = remainder
    #        index = index + 1
    #        n = n // 2
    #    binary = binary[::-1]
    #    reverse = 0
    #    for i in range(0, len(binary)):
    #        reverse = reverse + (2**i)*binary[i]
    #    return reverse
    
    # Faster bit wise operation
    def reverseBits(self, n: int) -> int:
        mask = 2**31
        result = 0
        for i in range(32):
            if n & mask:
                result = result + 2**i
            mask = mask >> 1
        return result

    def test_reverseBits(self):
        testcases = [0b00000010100101000001111010011100, 0b11111111111111111111111111111101]
        for testcase in testcases:
            print(testcase)
            print(self.reverseBits(testcase))
