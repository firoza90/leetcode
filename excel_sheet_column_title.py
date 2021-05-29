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
        colMapping = dict([map for map in enumerate(string.ascii_uppercase, start = 1)])
        LENGTH = 26
        result = ""
        while columnNumber > LENGTH:
            remainder = columnNumber % LENGTH
            result = result + colMapping[LENGTH if remainder == 0 else remainder]
            columnNumber = columnNumber // LENGTH if remainder != 0 else columnNumber // LENGTH  -1
        result = result + colMapping[columnNumber]
        return result[::-1]

    def test(self):
        testcases = [1, 28, 701, 2147483647, 52]
        for testcase in testcases:
            print(testcase)
            print(self.convertToTitle(testcase))

def main():
    sol = Solution()
    sol.test()
