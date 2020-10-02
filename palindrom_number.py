"""
https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
e.g.
Input: 121
Output: true
"""
def isPalindrome(x):
    if x < 0:
        return False
    xStr = str(x)
    reverseStr = xStr[::-1]
    return xStr == reverseStr

def isPalindrome_2(x):
    if x < 0 or ( x != 0 and x % 10 == 0):
        return False
    reverse = 0
    while (x > reverse):
        reverse = reverse * 10 + (x % 10)
        x = x // 10
    return x == reverse or x == (reverse // 10)

print(isPalindrome_2(1210))