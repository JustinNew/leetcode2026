# 470. Implement Rand10() Using Rand7()
# https://leetcode.com/problems/implement-rand10-using-rand7/
# Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a lot of extra memory.

# Example 1:
# Input: n = 1
# Output: [1]

# Example 2:
# Input: n = 2
# Output: [1,2]

# Example 3:
# Input: n = 3
# Output: [1,2,3]

# Key is to use the Von Neumann trick to generate a uniform random integer in the range [1, 10].
# We can use the Von Neumann trick to generate a uniform random integer in the range [1, 10].
# We can use the Von Neumann trick to generate a uniform random integer in the range [1, 10].

class Solution:
    def rand10(self):
        while True:
            x = (rand7() - 1) * 7 + rand7() # simulate uniform distribution between 1-49
            if x <= 40:
                return (x - 1) % 10 + 1 # simulate uniform distribution between 1-10