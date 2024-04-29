"""
    Given a string s, reverse only all the vowels in the string and return it.
    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

    Constraints: 1 <= s.length <= 3 * 105, s consist of printable ASCII characters.

    [Assignment 5](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        self.start = 0
        self.end = len(s) - 1
        self.word = list(s)

        while self.start < self.end:
            if self.word[self.start] in self.vowels:
                swap_first = self.word[self.start] # save current vowel to swap
                self.end = self.findNextVowel() # find index of matching vowel to swap

                # Swap vowels if vowel found
                if self.end != -1:
                    self.word[self.start] = self.word[self.end]
                    self.word[self.end] = swap_first
                    self.end -= 1 
                else: 
                    return ''.join(self.word)
                    
            self.start += 1
        return ''.join(self.word)

    def findNextVowel(self) -> int:
        for j in range(self.end, self.start, -1):
            if self.word[j] in self.vowels:
                return j

        return -1

