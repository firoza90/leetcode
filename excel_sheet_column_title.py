"""
https://leetcode.com/problems/excel-sheet-column-title/
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
.
.
.
Z -> 26
AA -> 27
AB -> 28 
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        import string
        colMapping = dict([map for map in enumerate(string.ascii_uppercase, start = 0)])
        LENGTH = 26
        result = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            remainder = columnNumber % LENGTH
            result = result + colMapping[remainder]
            columnNumber = columnNumber // LENGTH
        return result[::-1]

    def test(self):
        testcases = [1, 28, 701, 2147483647, 52]
        for testcase in testcases:
            print(testcase)
            print(self.convertToTitle(testcase))
