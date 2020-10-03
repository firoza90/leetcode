"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
Input: s = "{[]}"
Output: true
"""

def isValid(s):
    bMap = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
        }
    opening = ['(', '{', '[']
    stack = []

    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        else:
            if stack and bMap[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
    return not stack

print(isValid('{[]}()({()()})'))
