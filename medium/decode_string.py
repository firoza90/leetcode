
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
        pattern = ""
        repeat = 0
        for ch in s:
            if ch.isnumeric():
                repeat=(repeat*10)+int(ch)
            elif ch.isalpha():
                pattern+=ch
            elif ch == "[":
                repeats.append(repeat)
                patterns.append(pattern)
                repeat = 0
                pattern = ""
            elif ch == "]":
                repeat = repeats.pop()
                pattern = patterns.pop() + pattern *repeat 
                repeat = 0
        return pattern

    def test_decodeString(self):
        testcases = ["3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "100[leetcode]", "3[a2[c]]", "3[a]2[bc]",  "2[abc]3[cd]ef", "abc3[cd]xyz"]
        for testcase in testcases:
            print(testcase)
            print(self.decodeString(testcase))