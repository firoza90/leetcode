
"""
https://leetcode.com/problems/integer-to-roman/
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def intToRoman(self, num):
        map = {
            1: 'I',
            5: 'V',
            10: 'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
            }
        result = ''
        digits = (str(num))[::-1]
        positions = [1, 10, 100, 1000]
        for i, digit in enumerate(digits):
            position = positions[i]
            digit = int(digit)
            value = position * digit
            if value in map:
                result = map[value] + result
            elif digit in [4, 9]:
                base = position * (digit + 1)
                result = map[position] + map[base] + result
            elif digit in [1,2,3]:
                result = digit * map[position] + result
            elif digit in [6,7,8]:
                base = map[5*position]
                result = base + (digit-5) * map[position] + result
        return result

    def test_intToRoman(self):
        print(self.intToRoman(1994))

            

        