class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {}
        for i in range(len(nums)):
            if nums[i] in helper.keys():
                return [helper[nums[i]], i]
            else:
                helper[target - nums[i]] = i