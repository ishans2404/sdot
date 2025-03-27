# class Node:
#     def __init__(self, val: int):
#         self.val = val
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#     def add(self, val: int):
#         self.size += 1
#         if not self.head:
#             self.head = Node(val)
#             return
#         node = self.head
#         while node.next:
#             node = node.next
#         node.next = Node(val)
#     def print(self):
#         node = self.head
#         while node:
#             print(node.val, end=" ")
#             node = node.next
#         print()
#     def reverseK(self, k: int):
        

# def main():
#     ll = LinkedList()
#     inp = [1, 2, 3, 4, 5, 6, 7, 8]
#     for e in inp:
#         ll.add(e)
#     k = 3
#     ll.reverseK(k)
#     ll.print()

# main()




class Node:
    def __init__(self, data):
        self.data, self.next = data, None
 
def append(head, data):
    if not head: return Node(data)
    current = head
    while current.next: current = current.next
    current.next = Node(data)
    return head
 
def reverse_k_group(head, k):
    stack = []
    current = head
    prev_tail = None
    new_head = None
 
    while current:
        count = 0
        group_head = current
 
        while current and count < k:
            stack.append(current)
            current = current.next
            count += 1
 
        if count == k:
            if not new_head:
                new_head = stack[-1]
            if prev_tail:
                prev_tail.next = stack[-1]
 
            while stack:
                node = stack.pop()
                if stack:
                    node.next = stack[-1]
                else:
                    node.next = None
            prev_tail = group_head
        else:
            if prev_tail:
                prev_tail.next = group_head
            break
 
    return new_head
 
def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()
 
if __name__ == "__main__":
    values = list(map(int, input().split()))
    k = int(input())
    head = None
    for value in values:
        head = append(head, value)
 
    head = reverse_k_group(head, k)
    print_list(head)