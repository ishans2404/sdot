from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(s):
    if not s or s[0] == '-1':
        return None
    
    nodes = s.split()
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    
    while i < len(nodes):
        curr = queue.popleft()
        
        if i < len(nodes) and nodes[i] != '-1':
            curr.left = TreeNode(int(nodes[i]))
            queue.append(curr.left)
        else:
            curr.left = None
        i += 1
        
        if i < len(nodes) and nodes[i] != '-1':
            curr.right = TreeNode(int(nodes[i]))
            queue.append(curr.right)
        else:
            curr.right = None
        i += 1
    
    return root

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)

# Taking user input
t = int(input())
for _ in range(t):
    s = input().strip()
    root = build_tree(s)
    print("true" if is_bst(root) else "false")