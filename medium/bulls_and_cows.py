"""
https://leetcode.com/problems/bulls-and-cows/
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
"""

class Solution:
    # Slow
    #def getHint(self, secret: str, guess: str) -> str:
    #    cows, bulls = 0,0
    #    secret = [int(char) for char in secret]
    #    guess = [int(char) for char in guess]

    #    # find cows and remove from word
    #    bullIdx = []
    #    for i in range(0, len(secret)):
    #        if secret[i] == guess[i]:
    #            bulls = bulls + 1
    #            bullIdx.append(i)

    #    for idx in bullIdx[::-1]:
    #        secret.pop(idx)
    #        guess.pop(idx)

    #    guess = ''.join([str(s) for s in guess])
    #    for index, char in enumerate(secret):
    #        char = str(char)
    #        gIndex = guess.find(char)
    #        if gIndex < 0:
    #            continue
    #        cows = cows + 1
    #        guess = guess.replace(char, '', 1)

    #    return "%dA%dB" %(bulls, cows)

    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter

        counter = Counter(secret)
        bulls = cows = 0

        for idx, ch in enumerate(guess):
            if ch not in secret:
                continue

            # if its a bull
            if secret[idx] == ch: 
                bulls += 1
                # if a previous cow used up the one for bull, use that for bull, and remove from cow
                if counter[ch] <= 0:
                    cows -= 1
            else:
                # if secret still has available character, use it for cow
                if counter[ch] > 0:
                    cows += 1

            # update counter as it was used for bull or cow at this point
            counter[ch]-=1

        return "%dA%dB" %(bulls, cows)

    def test_getHint(self):
        testcases = [("1122", "0001"), ("11","11"), ("1807", "7810"), ("1123", "0111"), ("1", "0"), ("1", "1")]
        for testcase in testcases:
            print(testcase)
            secret, guess = testcase
            print(self.getHint(secret, guess))




        