"""
https://leetcode.com/problems/valid-palindrome/
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""

def isPalindrome(s: str) -> bool:
    import re
    string = re.sub(r'\W+', '', s).replace('_', '').lower()
    return string == string[::-1]

def run():
    testCases = ["A man, a plan, a canal: Panama", "race a car"]
    for testCase in testCases:
        print(testCase)
        print(isPalindrome(testCase))
        print("\n\n")