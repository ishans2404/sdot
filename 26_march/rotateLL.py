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