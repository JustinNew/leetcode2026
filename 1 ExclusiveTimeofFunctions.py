# 636. Exclusive Time of Functions
# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed.
# Each function has a distinct ID between 0 and n-1.
# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed.

# Example 1:
# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]
# Explanation:
# Function 0 starts at the beginning of time and executes for 3 units of time.
# Function 1 starts at the start time of function 0, and executes for 4 units of time.
# Function 0 resumes execution at the end of time 3 and executes for 2 units of time.
# Function 1 resumes execution at the end of time 6 and executes for 1 unit of time.
# So function 0 spends 3 + 2 = 5 units of total time executing, and function 1 spends 4 + 1 = 5 units of total time executing.

# Example 2:
# Input: n = 1, logs = ["0:start:0","0:end:0"]
# Output: [1]
# Explanation:
# Function 0 starts at the beginning of time and executes for 1 unit of time.
# Function 0 resumes execution at the end of time 0 and executes for 1 unit of time.
# So function 0 spends 1 + 1 = 2 units of total time executing.

# o(n) time complexity, o(n) space complexity
# Use a stack to store the functions and the times.
# If the function call starts, push the function and the time onto the stack.
# If the function call ends, pop the function and the time from the stack and calculate the time.

# Very tricky question
# Calculate by slots
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []

        prev = 0 # to store start time of recent funciton

        for i in range(len(logs)):
            iden, status, time_stamp = logs[i].split(":")
            iden = int(iden)
            time_stamp = int(time_stamp)
            
            if status == "start":
                if stack: # if there is already a fucntion running
                    top = stack[-1]
                    res[top] += time_stamp - prev

                stack.append(iden)
                prev = time_stamp
            else:
                top = stack.pop()

                res[top] += time_stamp - prev + 1 # +1 as it is  exclusive

                prev = time_stamp + 1 # +1 for same reason
        return res