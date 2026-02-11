class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[current] = nums[i]
                current += 1
        
        for i in range(current, len(nums)):
            nums[i] = 0

        return