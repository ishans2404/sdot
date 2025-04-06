from collections import deque

class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes or nodes[0] == "N":
        return None
    root = Node(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        current = queue.popleft()
        if nodes[i] != "N":
            current.left = Node(int(nodes[i]))
            queue.append(current.left)
        i += 1
        if i >= len(nodes):
            break
        if nodes[i] != "N":
            current.right = Node(int(nodes[i]))
            queue.append(current.right)
        i += 1
    return root

def right_view(root):
    if not root:
        return []
    view = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                view.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view

test_cases = int(input())
for _ in range(test_cases):
    node_vals = input().strip().split()
    tree_root = build_tree(node_vals)
    result = right_view(tree_root)
    print(" ".join(map(str, result)))