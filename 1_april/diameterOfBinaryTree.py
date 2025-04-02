# given bianry tree, diameter is the max distance between any two nodes in a tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def height(node: Node, diameter):
    if not node:
        return 0
    lh = height(node.left, diameter)
    rh = height(node.right, diameter)
    diameter[0] = max(diameter[0], lh + rh)
    return 1 + max(lh, rh)

def findDiameter(root: Node):
    diameter = [0]
    height(root, diameter)
    print(diameter[0])

def main():
    root = Node(6)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.right = Node(4)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    findDiameter(root)

main()