from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(lvlOrder):
    if not lvlOrder or lvlOrder[0] == "null":
        return None
    root = Node(int(lvlOrder[0]))
    que = deque([root])
    i = 1
    while i < len(lvlOrder):
        node = que.popleft()
        if i < len(lvlOrder) and lvlOrder[i] != "null":
            node.left = Node(int(lvlOrder[i]))
            que.append(node.left)
        i += 1
        if i < len(lvlOrder) and lvlOrder[i] != "null":
            node.right = Node(int(lvlOrder[i]))
            que.append(node.right)
        i += 1
    return root

def lowestCommonAncestor(root, p, q):
    if root.val == p or root.val == q:
        return root
    
    left = right = None
    if root.left:
        left = lowestCommonAncestor(root.left, p, q)
    if root.right:
        right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    else:
        return left or right
    
def main():
    lvlOrder = list(map(str, input().split()))
    root = buildTree(lvlOrder)
    p, q = int(input()), int(input())
    res = lowestCommonAncestor(root, p, q)
    print(res.val)

main()