"""
https://leetcode.com/problems/pascals-triangle/
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

def generate(numRows):
    result = []
    for i in range(0, numRows):
        row = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)
    return result

testCases = [3,4,5,6]
for testCase in testCases:
    print(testCase)
    print(generate(testCase))
    print("\n\n")
