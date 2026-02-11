# Counting Sort

from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    counts = {0:0, 1:0, 2:0}
    for num in nums:
        counts[num] += 1

    for i in range(counts[0]):
        nums[i] = 0
    for i in range(counts[0], counts[0] + counts[1]):
        nums[i] = 1
    for i in range(counts[0] + counts[1], len(nums)):
        nums[i] = 2

    print(nums)

# Two pointers + one index
# It is very tricky.
# Swap with 0, increase index and front pointer
# Swap with 2, decrease end pointer
# No need to increase index, because the swapped element is not checked
# When the element is 1, just increase index
def sortColors2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0:
        return

    i = 0
    front = 0
    end = len(nums) - 1
    while i <= end:
        if nums[i] == 0:
            temp = nums[i]
            nums[i] = nums[front]
            nums[front] = temp
            front += 1
            i += 1
        elif nums[i] == 2:
            temp = nums[i]
            nums[i] = nums[end]
            nums[end] = temp
            end -= 1
        else:
            i += 1

    return

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerobefore = 0
        twoafter = len(nums) - 1
        checking = 0

        while checking <= twoafter:
            if nums[checking] == 0:
                temp = nums[checking]
                nums[checking] = nums[zerobefore]
                nums[zerobefore] = temp
                checking += 1
                zerobefore += 1
            elif nums[checking] == 2:
                temp = nums[checking]
                nums[checking] = nums[twoafter]
                nums[twoafter] = temp
                twoafter -= 1
            else:
                checking += 1

        return 

sortColors2([2,0,2,1,1,0])