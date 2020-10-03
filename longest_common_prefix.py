"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: ["flower","flow","flight"]
Output: "fl"
"""

def longestCommonPrefix(strs):
    prefix = ''
    if not strs:
        return prefix
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    
    for x, y in zip(strs[0], strs[-1]):
        if x == y:
            prefix += x
        else:
            break
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))