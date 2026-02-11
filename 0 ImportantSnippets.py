from typing import List
from functools import cmp_to_key

# Customized compare function for sort
# Key is cmp_to_key, and customized compare function
def compare(n1, n2):
    if n1 + n2 > n2 + n1:
        return -1
    else:
        return 1

nums = [str(num) for num in [3, 30, 34, 5, 9]]
nums = sorted(nums, key=cmp_to_key(compare))
print(nums)

# Compare by second number in a tuple
# Key is lambda function
nums = [(1, 3), (3, 2), (2, 1)]
nums = sorted(nums, key=lambda x: x[1])
# another way to sort by second number in a tuple
nums.sort(key=lambda x: x[1])
print(nums)

from collections import defaultdict
# defaultdict is a dictionary that will return a default value if the key is not found
d = defaultdict(list)   # default value is []
d = defaultdict(int)    # default value is 0
d = defaultdict(set)    # default value is set()

# Python heap
# Python heapq is min heap
# There is no max heap in Python heapq
# To implement max heap, we can negate the values
import heapq

# Min heap example
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappop(heap)
print(heap)

# FIFO: Queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()
print(queue)

# LIFO: Stack  
# Using list as stack
stack = []
stack.append(1)
stack.append(2)
stack.pop()
print(stack)

# Check if a string is alphanumeric
str.isalnum()

# Check if a string is a number
str.isdigit()

# Check if a string is a letter
str.isalpha()

# Remove leading and trailing whitespace
str.strip()

# Replace whitespace with a character
str.replace(' ', 'a')

# Inf
a = float('inf') # positive infinity
a = float('-inf') # negative infinity   
a = float('nan') # not a number
import math
math.isinf(a) # True if a is infinity

# String operations
s = "Hello, World!"
s.lower()
s.upper()
s.replace('H', 'J')
s.split('/')
'+'.join(['Hello', 'World']) # 'Hello+World'
s.startswith('Hello')
s.endswith('World')
s.find('World')
s.count('World')
s.len

# Delete a key from a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
print(d)

# Dictionary key can be tuple.
# Tuple is immutable, so it can be used as a key in a dictionary.
# set is immutable, so it can be used as a key in a dictionary.
# list is mutable, so it cannot be used as a key in a dictionary.
s = 'hello'
d[tuple(sorted(s))] = 1

# Get the ASCII value of a character
ord('a')
ord('0')

########################################################
# List operations gotchas
# List append returns None
# List assignment is not a deep copy
# Do not use [0] * n to create a list with n zeros, use [0 for _ in range(n)] instead
########################################################
