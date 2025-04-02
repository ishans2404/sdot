# given bianry tree, diameter is the max distance between any two nodes in a tree                             
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]

    def height(self, node, diameter):
        if not node:
            return 0
        lh = self.height(node.left, diameter)
        rh = self.height(node.right, diameter)
        diameter[0] = max(diameter[0], lh + rh)
        return 1 + max(lh, rh)



if __name__ == "__main__":
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    solution = Solution()

    diameter = solution.diameterOfBinaryTree(root)
    print("The diameter of the binary tree is:", diameter)
                                
                            