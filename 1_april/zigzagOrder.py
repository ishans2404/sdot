# given bianry tree, print each left, first left to right, then right to left and the same
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagOrder(root: Node):
    que = deque()
    que.append(root)
    flag = True
    while que:
        level = []
        for i in range(len(que)):
            node = que.popleft()
            level.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        if not flag:
            level = level[::-1]
        for i in level:
            print(i, end=" ")
        print()
        flag = not flag

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    zigzagOrder(root)

main()