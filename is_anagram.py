"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s:
            if c in map:
                map[c] = map[c] + 1
            else:
                map[c] = 1
        for c in t:
            if c in map:
                map[c] = map[c] - 1
            else:
                return False

        mismatch = set([value for value in map.values() if value != 0])
        if mismatch:
            return False
        return True

    def test_isAnagram(self):
        testcases = [("anagram", "nagaram"), ( "rat", "car")]
        for test in testcases:
            print(test)
            print(self.isAnagram(test[0], test[1]))





