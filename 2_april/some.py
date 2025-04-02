from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(lvlOrder):
    if not lvlOrder or lvlOrder[0] == 'N':
        return None
    root = Node(int(lvlOrder[0]))
    que = deque([root])
    i = 1
    while i < len(lvlOrder):
        node = que.popleft()
        if i < len(lvlOrder) and lvlOrder[i] != 'N':
            node.left = Node(int(lvlOrder[i]))
            que.append(node.left)
        i += 1
        if i < len(lvlOrder) and lvlOrder[i] != 'N':
            node.right = Node(int(lvlOrder[i]))
            que.append(node.right)
        i += 1
    return root


def main():
    lvlOrder = list("12534N6NNNNNNN7")
    print(lvlOrder)
    root = buildTree(lvlOrder)
    print(root)

main()