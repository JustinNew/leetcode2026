""" Input: 
A method getRandom01Biased() that generates a random integer in [0, 1], 
where 0 is generated with probability p and 1 is generated with probability (1-p) 

Output: 
A method getRandom06Uniform() that generates a random integer in [0, 6] with uniform probability """ 

# 解题思路是:
# 1 - 先debias coin 
# 2 - bit manipulation, 用randomize每一个bit位置, 
# 三个bit simulate uniform distribution between 0-6 

# Step 1 — Debias (Von Neumann trick)
# 00 → discard
# 11 → discard
# 01 → 0
# 10 → 1
# → gives fair coin

# Step 2 — Build number using bits

# You generate 3 fair bits:
# 000 → 0
# 001 → 1
# ...
# 110 → 6
# 111 → discard (reject)
