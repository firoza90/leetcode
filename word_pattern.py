"""
https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False
        map = {}
        for i in range(0,len(pattern)):
            if pattern[i] in map:
                if map[pattern[i]] != s[i]:
                    return False
            else:
                map[pattern[i]] = s[i]
        return True

    def test_wordPattern(self):
        testcases = [("abba", "dog cat cat dog"), ("abba", "dog cat cat fish"), ("aaaa", "dog cat cat dog"), ("abba", "dog dog dog dog")]
        for testcase in testcases:
            print(testcase)
            pattern, s = testcase
            print(self.wordPattern(pattern, s))