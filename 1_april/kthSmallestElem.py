# given binary tree, find kth smallest element
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def kthSmallest(root: Node, k: int):
    count = 1
    def inorder(node: Node):
        nonlocal count
        if not node:
            return
        inorder(node.left)
        if count == k:
            print(node.val)
        count += 1
        inorder(node.right)
    inorder(root)


def main():
    root = Node(6)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(9)
    kthSmallest(root, k=1)

main()