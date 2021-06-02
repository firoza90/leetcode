"""
https://leetcode.com/problems/insert-interval/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their START times.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

class Solution:
    def insert(self, intervals, newInterval):
        START = 0
        END = 1
        n = len(intervals)
        result = []

        if n == 0:
            return [newInterval]

        # arrange in increasing order of START
        i = 0
        while i < n:
            interval = intervals[i]
            if interval[START] >= newInterval[START]:
                intervals.insert(i, newInterval)
                break
            i = i+1
        if i == n:
            intervals.append(newInterval)

        # merge intervals now
        curr = intervals[0]
        for interval in intervals[1:]:
            if interval[START] > curr[END]:
                result.append(curr)
                curr = interval
            else:
                curr[END] = max(interval[END], curr[END])
        result.append(curr)
        return result

    def test_insert(self):
        testcases = [([[1,3],[6,9]], [2,5]), ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), ([], [5,7]), ([[1,5]], [2,3]), ([[1,5]], [2,7])]
        for testcase in testcases:
            print(testcase)
            intervals, newInterval = testcase
            print(self.insert(intervals, newInterval))


        