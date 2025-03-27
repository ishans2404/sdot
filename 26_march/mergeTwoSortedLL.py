class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, val: int):
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

def merge(a: LinkedList, b: LinkedList):
    if not a.head:
        return b
    if not b.head:
        return a
    nodea, nodeb = a.head, b.head
    ll = LinkedList()
    while nodea and nodeb:
        if nodea.val < nodeb.val:
            ll.add(nodea.val)
            nodea = nodea.next
        else:
            ll.add(nodeb.val)
            nodeb = nodeb.next
    while nodea:
        ll.add(nodea.val)
        nodea = nodea.next
    while nodeb:
        ll.add(nodeb.val)
        nodeb = nodeb.next
    return ll

def main():
    ll1, ll2 = LinkedList(), LinkedList()
    num1 = input()
    inp1 = map(int, input().split())
    num2 = input()
    inp2 = map(int, input().split())
    for e1 in inp1:
        ll1.add(e1)
    for e2 in inp2:
        ll2.add(e2)

    res = merge(ll1, ll2)
    res.print()

main()