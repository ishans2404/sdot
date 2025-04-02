# given bianry tree, with each 1 <= node.val <= 9, find sum of all numbers which are formed from root to leaf paths 
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSum(root: Node):
    que = deque()
    que.append(root)
    total = 0
    while que:
        for _ in range(len(que)):
            node = que.popleft()
            if node.left:
                node.left.val += node.val * 10
                que.append(node.left)
            if node.right:
                node.right.val += node.val * 10
                que.append(node.right)
            if not node.left and not node.right:
                print(node.val, end=" ")
                total += node.val
    print("= ", total)

def bfs(root: Node):
    que = deque()
    que.append(root)
    while que:
        lvl = []
        for _ in range(len(que)):
            node = que.popleft()
            lvl.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        print(lvl)

def main():
    root = Node(6)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.right = Node(4)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    findSum(root)

main()