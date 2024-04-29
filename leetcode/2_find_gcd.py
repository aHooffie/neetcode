"""
    For two strings s and t, we say "t divides s", if and only if s = t + t + t + ... + t + t, i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
    Constraints: 1 <= str1.length, str2.length <= 1000
    [Assignment 2](https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75)
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # Check if they contain the same concatenation
            return ""

        if len(str1) == len(str2): # Check if strings are identical
            return str1

        if len(str1) > len(str2): # Apply Euclid algorithm of gcd to the strings
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
