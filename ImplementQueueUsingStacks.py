# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyStack:

    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        if len(self.left) > 0:
            self.left.append(x)
        elif len(self.right) > 0:
            self.right.append(x)
        else:
            self.left.append(x)

    def pop(self) -> int:
        if len(self.left) > 0:
            val = self.left[-1]
            self.right = [_ for _ in self.left[:-1]]
            self.left = []
            return val
        elif len(self.right) > 0:
            val = self.right[-1]
            self.left = [_ for _ in self.right[:-1]]
            self.right = []
            return val
        else:
            return None

    def top(self) -> int:
        if len(self.left) > 0:
            return self.left[-1]
        elif len(self.right) > 0:
            return self.right[-1]
        else:
            return None       

    def empty(self) -> bool:
        if len(self.left) == 0 and len(self.right) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()