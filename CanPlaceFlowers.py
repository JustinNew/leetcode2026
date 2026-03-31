# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# Example 3:
# Input: flowerbed = [0,1,0,1,0,1,0,0], n = 0
# Output: true

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 0: no plant
        # 0, 0: no plant
        # 0, 0, 0: plant 1
        # 0, 0, 0, 0: plant 1
        # (No. 0 - 1) // 2
        count = 1
        result = 0
        for num in flowerbed:
            if num == 1:
                if count >= 1:
                    result += (count - 1) // 2
                count = 0
            else:
                count += 1

        if count >= 1:
            result += count // 2

        return result >= n