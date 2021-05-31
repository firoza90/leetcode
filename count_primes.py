"""
https://leetcode.com/problems/count-primes/
Count the number of prime numbers less than a non-negative number, n.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0

        if n in [0, 1]:
            return count

        isPrime = [True] * n
        isPrime[0], isPrime[1] = False, False

        for i in range(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                continue
            for j in range(i*i, n, i):
                isPrime[j] = False

        for i in range(2, n):
            if isPrime[i]:
                count = count + 1
        return count

    def test_countPrimes(self):
        testcases = [10, 0, 1]
        for testcase in testcases:
            print(self.countPrimes(testcase))

