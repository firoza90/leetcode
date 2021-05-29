"""
https://leetcode.com/problems/excel-sheet-column-number/"
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string
        colMapping = dict([map[::-1] for map in enumerate(string.ascii_uppercase, start = 1)])
        LENGTH = 26
        result = 0
        columnTitle = columnTitle[::-1]
        for index, letter in enumerate(columnTitle):
            result = result + (LENGTH**index)*colMapping[letter]
        return result

    def test(self):
        testcases = ['A', 'AB', 'ZY', 'FXSHRXW', 'AZ']
        for testcase in testcases:
            print(testcase)
            print(self.titleToNumber(testcase))

def main():
    sol = Solution()
    sol.test()