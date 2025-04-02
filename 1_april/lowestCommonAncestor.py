class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)
    res = lowestCommonAncestor(root, 1, 4)
    print(res.val)

main()