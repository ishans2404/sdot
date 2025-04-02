# given bianry tree, print each left, first left to right, then right to left and the same
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
        flag = not flag

def main():
    lvlOrder = list(map(str, input().split()))
    root = buildTree(lvlOrder)
    zigzagOrder(root)

main()