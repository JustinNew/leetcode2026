# https://leetcode.com/problems/largest-number/
# Need to write a customized comparing function for the sort function
# There is no better way to solve this problem.

from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:
    for i, num in enumerate(nums):
        nums[i] = str(num)

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    nums = sorted(nums, key=cmp_to_key(compare))

    return str(int("".join(nums)))

def largestNumber2(nums: List[int]) -> str:
    for i, num in enumerate(nums):
        nums[i] = str(num)

    def mergeSort(nums):
        print("nums")
        print(nums)
        if len(nums) <= 1:
            return nums
        
        large = []
        small = []

        pivot = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + pivot < pivot + nums[i]:
                large.append(nums[i])
            else:
                small.append(nums[i])

        print("large")
        print(large)
        print("small")
        print(small)
        if len(large) > 1:
            large = mergeSort(large)
        if len(small) > 1:
            small = mergeSort(small)

        return small + [pivot] + large

    nums = mergeSort(nums)

    return str(int("".join(nums)))

print(largestNumber2([10, 2]))
print(largestNumber2([3, 30, 34, 5, 9]))
print(largestNumber2([1]))
print(largestNumber2([10]))
