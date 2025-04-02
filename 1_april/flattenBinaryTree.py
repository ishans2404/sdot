# given binary tree, flatten tree to linked list (same order as preorder traversal)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def flatten(root: Node):
    preorderTraversal = []
    def preorder(node: Node):
        if not node:
            return
        preorderTraversal.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    if not preorderTraversal:
        return None
    root = Node(preorderTraversal[0])
    node = root
    for el in preorderTraversal[1:]:
        node.left = None
        node.right = Node(el)
        node = node.right
    node = root
    while node:
        print(node.val, end=" ")
        node = node.right
    return root

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)
    flatten(root)

main()