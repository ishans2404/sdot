class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, *args):
        print(args)
        if len(args) > 0 and isinstance(args[0], Node):
            node = args[0]
            while node:
                self.add(node.val)
                node = node.next
        else:
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
    def rotateList(self, k: int):
        k %= self.size
        if not k:
            return
        head = self.head
        node = self.head
        for i in range(self.size - k - 1):
            node = node.next
        self.head = node.next
        tmp = self.head
        node.next = None
        while tmp.next:
            tmp = tmp.next
        tmp.next = head


def reverse(ll: LinkedList):
    prev = None
    curr = ll.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return ll


# def main():
#     ll = LinkedList()
#     inp = [1, 2, 3, 4, 5, 6]
#     for e in inp:
#         ll.add(e)
#     k = 5
#     ll.rotateList(k)
#     ll.print()

# main()


def main():
    ll = LinkedList()
    inp = map(int, input().split())
    m = input()
    k = int(input())
    for e in inp:
        ll.add(e)
    ll.rotateList(k)
    ll.print()

main()