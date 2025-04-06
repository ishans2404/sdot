class Queue:
    def __init__(self):
        self.que = []
        self.size = 0
    def enqueue(self, val):
        self.que.append(val)
        self.size += 1
    def dequeue(self):
        if self.size > 0:
            val = self.que.pop(0)
            self.size -= 1
            return val
        return -1

que = Queue()
n = int(input())
for _ in range(n):
    q = list(map(int, input().split()))
    if len(q) > 1:
        que.enqueue(q[1])
    else:
        print(que.dequeue(), end = " ")