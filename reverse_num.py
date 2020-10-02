""" 
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.
e.g.
Input: 123
Output: 321
"""

def reverse(x):
    reverse = 0
    sign = True if x < 0 else False
    x = abs(x)
    while ( x != 0):
        digit = x % 10
        x = x // 10
        reverse = reverse * 10 + digit
        if (reverse > 2**31-1) or (reverse < -(2**31)):
            return 0
    return reverse if not sign else -reverse

print(reverse(-123))