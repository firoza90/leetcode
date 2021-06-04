"""
https://leetcode.com/problems/valid-square/
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
"""

class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        from collections import Counter
        lengths = []
        X = 0
        Y = 1
        points = [p1, p2, p3, p4]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                length = (points[i][X]-points[j][X])**2 + (points[i][Y]-points[j][Y])**2
                lengths.append(length)
        counter = Counter(lengths)
        if len(counter) != 2 or 0 in lengths:
            return False
        for key in counter:
            if counter[key] not in [4,2]:
                return False
        return True

    def test_validSquare(self):
        testcases = [([0,0], [5,0], [5,4], [0,4]), ([0,0], [1,1], [1,0], [1,1]), ([0,0], [1,1], [1,0], [0,1]), ([0,0], [1,1], [1,0], [0,12]), ([1,0], [-1,0], [0,1], [0,-1])]
        for testcase in testcases:
            print(testcase)
            print(self.validSquare(*testcase))

        