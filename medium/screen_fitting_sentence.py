"""
https://leetcode.com/problems/sentence-screen-fitting/
Given a rows x cols screen and a sentence represented as a list of strings, 
return the number of times the given sentence can be fitted on the screen.
The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. 
A single space must separate two consecutive words in a line.
Example:
Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
"""

class Solution:
    # Time Complexity : O(row* (col/average length)) - slow
    #def wordsTyping(self, sentence, rows: int, cols: int) -> int:
    #    total = idx = i = 0
    #    while (i < rows):
    #        s = sentence[idx]
    #        idx = (idx+1)%len(sentence)
    #        if idx == 0:
    #            total+=1
    #        while (len(s) + len(sentence[idx]) + 1) <= cols:
    #            s += " " + sentence[idx]
    #            idx = (idx+1)%len(sentence)
    #            if idx == 0:
    #                total+=1
    #        i+=1
    #        print(s)
    #    return total

    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        # join the words with a space at end, as gap between repeated statements is required
        string = " ".join(sentence) + " "
        # index keeps track of valid words processed at any point
        index = 0
        for i in range(0, rows):
            # try to fit as many words possible in one row
            index += cols
            # if the first character in the next row is not a whitespace, it means we have performed line break in between a word
            # In this case, decrease the index to the start of the broken space
            while string[index%len(string)] != " ":
                index-=1
            # ignore the white space in the first character of the next line by going to the next elelement
            index+=1
        return index//len(string)


    def test_wordsTyping(self):
        testcases = [(["f","p","a"], 8, 7), (["a", "bcd", "e"], 3, 6), (["hello","world"], 2, 8), (["i","had","apple","pie"], 4, 5), ]
        for testcase in testcases:
            print(testcase)
            sentence, rows, cols = testcase
            print(self.wordsTyping(sentence, rows, cols))


        