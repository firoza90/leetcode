
"""
https://leetcode.com/problems/decode-string/
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        patterns = []
        repeats = []
        partial = ""
        repeat = 0
        for ch in s:
            if ch.isalpha():
                partial+=ch
            if ch.isnumeric():
                repeat+=(repeat*10)+int(ch)
                patterns.append(partial)
                partial = ""
            if ch == "[":
                repeats.append(repeat)
            if ch == "]":
                string = patterns.pop() * 

    def test_decodeString(self)