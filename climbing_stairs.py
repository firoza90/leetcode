
"""
https://leetcode.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

def climbStairs(n):
    result = [1,2]

    for i in range(2, n):
        result.insert(i, result[i-1] + result[i-2])
    return result[-1]

print(climbStairs(5))