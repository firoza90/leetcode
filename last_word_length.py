"""
https://leetcode.com/problems/length-of-last-word/
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word 
(last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.
Input: "Hello World"
Output: 5
"""

def lengthOfLastWord(s):
    words = [word for word in s.split(" ") if word]
    return 0 if not words else len(words[-1])

print(lengthOfLastWord("Hello World "))
print(lengthOfLastWord("a "))
print(lengthOfLastWord(" "))