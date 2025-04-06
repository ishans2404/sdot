class Stk:
    def __init__(self):
        self.stk = []
        self.size = 0
    def push(self, val):
        self.stk.append(val)
        self.size += 1
    def pop(self):
        if self.size > 0:
            val = self.stk.pop()
            self.size -= 1
            return val
        return -1

stack = Stk()
n = int(input())
for _ in range(n):
    q = list(map(int, input().split()))
    if len(q) > 1:
        stack.push(q[1])
    else:
        print(stack.pop(), end = " ")