class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add(self, val: int):
        self.size += 1
        if not self.head:
            self.head = Node(val)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)
    def print(self):
        node = self.head
        while node:
            print(node.val, end=" ")
            node = node.next
        print()
    def evenOddSeparate(self):
        if self.size <= 1:
            return
        even_head = even_tail = odd_head = odd_tail = None
        curr = self.head
        while curr:
            if not curr.val & 1:
                if not even_head:
                    even_head = even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = even_tail.next
            else:
                if not odd_head:
                    odd_head = odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = odd_tail.next
            curr = curr.next
        if even_tail:
            even_tail.next = odd_head
        else:
            even_head = odd_head
        if odd_tail:
            odd_tail.next = None
        self.head = even_head

def main():
    ll = LinkedList()
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    for e in inp:
        ll.add(e)
    ll.evenOddSeparate()
    ll.print()

main()