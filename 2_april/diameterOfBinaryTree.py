# given bianry tree, diameter is the max distance between any two nodes in a tree
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
    
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.height(root, diameter)
        return diameter[0] + 1

    def height(self, node, diameter):
        if not node:
            return 0
        lh = self.height(node.left, diameter)
        rh = self.height(node.right, diameter)
        diameter[0] = max(diameter[0], lh + rh)
        return 1 + max(lh, rh)

if __name__ == "__main__":
    lvlOrder = list(map(str, input().split()))
    root = buildTree(lvlOrder)
    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)
    print(diameter)
                                