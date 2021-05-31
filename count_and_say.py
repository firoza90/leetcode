"""
https://leetcode.com/problems/count-and-say/
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
You can do so recursively, in other words from the previous member read off the digits, 
counting the number of digits in groups of the same digit.
Note: Each term of the sequence of integers will be represented as a string.
"""

class Solution:
    def countAndSay(self, n):
        # base condition
        if n == 1:
            return "1"

        prevResult = self.countAndSay(n-1)
        result = ""
        count = 0
        curr = prevResult[0]

        for digit in prevResult:
            if digit == curr:
                count += 1
            else:
                result += str(count) + curr
                curr = digit
                count = 1
        return result + str(count) + curr

    def countAndSay_iter(n):
        result = "1"
        c = 2
        while (c <= n):
            count = 1
            curr = ""
            for i in range(1, len(result)):
                if result[i] == result[i-1]:
                    count+=1
                else:
                    temp += str(count) + result[i-1]
                    count+=1
            result = temp + str(count) + result[-1]
            c+=1
        return result

    def test_countAndSay(self):
        for i in range(1, 30):
            print(self.countAndSay(i))




