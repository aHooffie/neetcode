"""
    You have a long flowerbed in which some of the plots are planted, and some are not.
    However, flowers cannot be planted in adjacent plots.
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
    and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

    Constraints: 1 <= flowerbed.length <= 2 * 104, flowerbed[i] is 0 or 1. 
    There are no two adjacent flowers in flowerbed and 0 <= n <= flowerbed.length.

    [Assignment 4](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range (0, len(flowerbed)):
            if flowerbed[i] == 0: # Check current position
                if i + 1 > len(flowerbed) - 1 or flowerbed[i + 1] == 0: # Check right side
                    if i - 1 < 0 or flowerbed[i - 1] == 0: # Check left side
                        flowerbed[i] = 1
                        n -= 1

        # This check could be placed inside the for loop to break it off earlier,
        # but this did not enhance speed with the given tests.
        if n <= 0:
            return True
        else:
            return False
