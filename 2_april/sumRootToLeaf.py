# given bianry tree, with each 1 <= node.val <= 9, find sum of all numbers which are formed from root to leaf paths 
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(lvlOrder):
    if not lvlOrder or lvlOrder[0] == "N":
        return None
    root = Node(int(lvlOrder[0]))
    que = deque([root])
    i = 1
    while i < len(lvlOrder):
        node = que.popleft()
        if i < len(lvlOrder) and lvlOrder[i] != "N":
            node.left = Node(int(lvlOrder[i]))
            que.append(node.left)
        i += 1
        if i < len(lvlOrder) and lvlOrder[i] != "N":
            node.right = Node(int(lvlOrder[i]))
            que.append(node.right)
        i += 1
    return root

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
                total += node.val
    print(total)

def main():
    lvlOrder = list(map(str, input().split()))
    root = buildTree(lvlOrder)
    findSum(root)

main()