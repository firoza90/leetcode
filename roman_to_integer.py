"""
https://leetcode.com/problems/roman-to-integer/
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
Input: "MCMXCIV"
Output: 1994
"""

def romanToInt(s):
    cMap = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
        }

    sMap = { 
        'CM' : 900,
        'CD' : 400,
        'XC' : 90,
        'XL' : 40,
        'IX' : 9,
        'IV' : 4
        }

    num = 0

    for rNum in sMap.keys():
        if rNum in s:
            s = s.replace(rNum, '')
            num += sMap[rNum]

    for rNum in cMap.keys():
        if rNum in s:
            n = s.count(rNum)
            num += n * cMap[rNum]
            s = s.replace(rNum, '')
    return num

print(romanToInt('LIX'))
print(romanToInt('MCMXCIV'))
