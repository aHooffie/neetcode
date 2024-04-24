"""
    You are given two strings word1 and word2.
    Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.
    Constraints: 1 <= word1.length, word2.length <= 100
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        len1, len2 = len(word1), len(word2)
        if len1 > len2:
            for i in range (0, len2):
                result += word1[i]
                result += word2[i]
            result += word1[len2:]
        else:
            for i in range (0, len1):
                result += word1[i]
                result += word2[i]
            result += word2[len1:]
        return result