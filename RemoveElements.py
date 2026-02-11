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