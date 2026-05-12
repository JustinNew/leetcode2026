# 27. Remove Element
# Given an array nums and a value val, 
# remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. 
# It doesn't matter what you leave beyond the new length.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,3,0,4,_,_,_]


from typing import List

def removeElement(nums: List[int], val: int) -> int:
    if len(nums) == 0: 
        return 0

    if len(nums) == 1:
        if nums[0] == val:
            return 0
        else:
            return 1

    begin = 0 
    end = len(nums) - 1
    while begin < end:
        if nums[begin] != val:
            begin += 1
        else:
            dummy = nums[begin]
            nums[begin] = nums[end]
            nums[end] = dummy
            end -= 1
        
    if nums[begin] == val:
        return begin
    else:
        return begin + 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[current] = nums[i]
                current += 1

        return current

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return

        current = 0
        for ndx in range(len(nums)):
            if nums[ndx] == val:
                continue
            else:
                nums[current] = nums[ndx]
                current += 1

        return current

# 20260511 Solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use two pointers
        # current and front

        current = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[current] = nums[i]
                current += 1

        return current