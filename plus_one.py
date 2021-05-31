"""
https://leetcode.com/problems/plus-one/
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        carry = 1
        for i in range(0, len(digits)):
            if carry == 0:
                break
            else:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i]+=1
                    carry = 0
        if carry == 1:
            digits.append(1)
        return digits[::-1]

    def test_plusOne(self):
        print(self.plusOne([1,2,3]))
        print(self.plusOne([4,3,2,1]))
        print(self.plusOne([0]))
        print(self.plusOne([9]))

