"""
https://leetcode.com/problems/pascals-triangle-ii/
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
"""

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    prev = [1,1]
    for i in range(2, rowIndex+1):
        curr = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                curr.append(1)
            else:
                curr.append(prev[j-1] + prev[j])
        prev = curr
    return curr

testCases = [3,4,5,6]
for testCase in testCases:
    print(testCase)
    print(getRow(testCase))
    print("\n\n")
