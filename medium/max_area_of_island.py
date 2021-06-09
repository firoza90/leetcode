"""
https://leetcode.com/problems/max-area-of-island/
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution:

    def area(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.seen[row][col] or not self.grid[row][col]:
            return 0
        self.seen[row][col] = True
        return 1 + self.area(row-1, col) + self.area(row+1, col) + self.area(row, col-1) + self.area(row, col+1)
    
    def maxAreaOfIsland(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.seen = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        maxArea = 0
        for i in range(self.rows):
            for j in range(self.cols):
                maxArea = max(maxArea, self.area(i, j))
        return maxArea

    def print_testcase(self, testcase):
        for row in testcase:
            print(row)
        print()

    def test_maxAreaOfIsland(self):
        testcases = [[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], [[0,0,0,0,0,0,0,0]]]
        for testcase in testcases:
            self.print_testcase(testcase)
            print(self.maxAreaOfIsland(testcase))
        