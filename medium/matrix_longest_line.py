"""
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
The line could be horizontal, vertical, diagonal, or anti-diagonal.
"""

class Solution:
    def longestLine(self, mat) -> int:
        rows = len(mat)
        cols = len(mat[0])
        sol = [[[0,0,0,0] for i in range(cols)] for j in range(0, rows)]
        result = 0

        for i in range(0, rows):
            for j in range(0, cols):
                if not mat[i][j]:
                    continue

                sol[i][j][0] = 1 if j == 0 else sol[i][j-1][0]+1
                sol[i][j][1] = 1 if i == 0 else sol[i-1][j][1]+1
                sol[i][j][2] = 1 if ( i == 0 or j == cols-1) else sol[i-1][j+1][2]+1
                sol[i][j][3] = 1 if ( i == 0 or j == 0) else sol[i-1][j-1][3]+1
                result = max(result, sol[i][j][0], sol[i][j][1], sol[i][j][2], sol[i][j][3])
        return result

    def print_testcase(self, testcase):
        for row in testcase:
            print(row)

    def test_longestLine(self):
        testcases = [[[0,0,0],[0,1,0],[1,1,1]], [[0,1,1,0],[0,1,1,0],[0,0,0,1]],  [[1,1,1,1],[0,1,1,0],[0,0,0,1]]]
        for testcase in testcases:
            self.print_testcase(testcase)
            print(self.longestLine(testcase))
            