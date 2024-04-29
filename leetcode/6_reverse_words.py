"""
    Given an input string s, reverse the order of the words.
    A word is defined as a sequence of non-space characters.
    The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.
    Constraints: 1 <= s.length <= 104. s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.


    [Assignment 6](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ') # Split string into words
        words = [word.strip() for word in words if word] # Strip whitespaces
        words.reverse() # Reverse the order of the words
        return ' '.join(words) # Return a new string with singular whitespace