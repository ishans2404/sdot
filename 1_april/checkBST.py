# given binary tree, check if it is bst?
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def validate(root: Node):
    last = root.val
    def inorder(node: Node):
        if not node:
            return
        inorder(node.left)
        print(node.val, end = " ")
        inorder(node.right)
    inorder(root)
    print("valid")


def main():
    root = Node(6)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(9)
    validate(root)

main()