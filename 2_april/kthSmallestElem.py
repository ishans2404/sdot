# your code goes here
class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def construct_bst(level_order):
    if not level_order or level_order[0] == "N":
        return None

    root = TreeNode(int(level_order[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        if i < len(level_order) and level_order[i] != "N":
            node.left = TreeNode(int(level_order[i]))
            queue.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] != "N":
            node.right = TreeNode(int(level_order[i]))
            queue.append(node.right)
        i += 1

    return root

def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1
        if count == k:
            return current.val

        current = current.right

    return -1  

level_order = input().split()
k = int(input().strip())

bst_root = construct_bst(level_order)
print(kth_smallest(bst_root, k))