from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(lvlOrder):
    if not lvlOrder or lvlOrder[0] == 'N':
        return None
    lvlOrder = lvlOrder.replace("N", " N ").split()
    root = Node(int(lvlOrder[0]))
    queue = deque([root])
    i = 1
    while i < len(lvlOrder):
        node = queue.popleft()
        
        if i < len(lvlOrder) and lvlOrder[i] != 'N':
            node.left = Node(int(lvlOrder[i]))
            queue.append(node.left)
        i += 1
        
        if i < len(lvlOrder) and lvlOrder[i] != 'N':
            node.right = Node(int(lvlOrder[i]))
            queue.append(node.right)
        i += 1
    return root


def flatten(root):
    if not root:
        return None
    
    stack = [root]
    prev = None
    
    while stack:
        curr = stack.pop()
        
        if prev:
            prev.right = curr
            prev.left = None
        
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        
        prev = curr
    
    return root


def printFlattened(root):
    while root:
        print(root.val, end=" ")
        root = root.right
    print()


def main():
    lvlOrder = input().strip()
    root = buildTree(lvlOrder)
    flatten(root)
    printFlattened(root)

if __name__ == "__main__":
    main()
