"""
https://leetcode.com/problems/meeting-rooms-ii/
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

class Solution:
    def minMeetingRooms(self, intervals):
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
        times.sort()
        result, sum = 0, 0
        for time, value in times:
            sum = sum+value
            result = max(sum, result)
        return result

    def test_minMeetingRooms(self):
        testcases = [[[9,10],[4,9],[4,17]], [[0,100], [5, 50], [6, 20], [30, 40]], [[0,30],[5,10],[15,20]], [[7,10],[2,4]]]
        for testcase in testcases:
            print(testcase)
            print(self.minMeetingRooms(testcase))

        