class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_list_to_bst(head):
    def find_middle(left, right):
        if left == right:
            return None
        slow = fast = left
        prev = None
        while fast and fast.next and fast != right and fast.next != right:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
    
    def convert_to_bst(left, right):
        if left == right:
            return None
        mid = find_middle(left, right)
        if mid is None:
            return None
        root = TreeNode(mid.val)
        root.left = convert_to_bst(left, mid)
        root.right = convert_to_bst(mid.next, right)
        return root
    
    return convert_to_bst(head, None)

def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(int(values[0]))
    curr = head
    for val in values[1:]:
        curr.next = ListNode(int(val))
        curr = curr.next
    return head

values = list(map(int, input().split()))
head = create_linked_list(values)
root = sorted_list_to_bst(head)
print(" ".join(map(str, preorder_traversal(root))))