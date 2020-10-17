
"""
https://leetcode.com/problems/add-binary/
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"
"""
def addBinary(a, b):
    result = ""
    carry = 0
    a = a[::-1]
    a = [int(item) for item in a]
    b = b[::-1]
    b = [int(item) for item in b]

    if len(a) < len(b):
        a, b = b, a

    for digit_a, digit_b in zip(a,b):
        sum = digit_a + digit_b + carry
        result = str(sum % 2) + result
        carry = sum // 2
    if len(a) != len(b):
        for i in range(len(b), len(a)):
            sum = a[i] + carry
            result = str(sum % 2) + result
            carry = sum // 2
    if carry == 1:
        result = "1" + result
    return result

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
