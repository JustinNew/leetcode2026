# 528. Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/

# Example 1:
# Input: w = [1,3], k = 1
# Output: 1
# Explanation: The sum of the weights is 1 + 3 = 4.
# The probability of picking index 0 is 1 / 4 = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / 4 = 0.75 (i.e., 75%).
# Example 2:
# Input: w = [1,3], k = 2
# Output: 1
# Explanation: The sum of the weights is 1 + 3 = 4.

# The binary search is not needed, as the overall time complexity will be o(N) anyway.
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        low, high = 0, len(self.prefix) - 1
        while low < high:
            mid = (low + high) // 2
            if self.prefix[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low

# Do not need to use binary search.
# Do a linear scan to find the index of the target.
class Solution:

    def __init__(self, w: List[int]):
        self._arr = []
        cum_sum = 0
        for n in w:
            cum_sum += n
            self._arr.append(cum_sum)

        self._arr = [n / cum_sum for n in self._arr]

    def pickIndex(self) -> int:
        import random
        num = random.random()

        for i in range(len(self._arr)):
            if self._arr[i] >= num:
                return i