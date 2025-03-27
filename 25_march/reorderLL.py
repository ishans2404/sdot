# incomplete
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, *args):
        # if len(args) > 0 and isinstance(args[0], Node):
        #     node = args[0]
        #     while node:
        #         self.add(node.val)
        #         node = node.next
        # else:
        #     self.head = None
        #     self.size = 0
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
    def reorder(self):
        if self.size <= 1:
            return
        count = 0
        node = self.head
        while count < self.size // 2 - 1:
            count += 1
            node = node.next
        tmp = node.next
        node.next = None
        stk = []
        while tmp:
            stk.append(tmp.val)
            tmp = tmp.next
        count = 0
        ll = LinkedList()
        node = self.head
        while count < self.size:
            if node:
                ll.add(node.val)
                node = node.next
                count += 1
            if stk:
                ll.add(stk.pop())
                count += 1
        self.head = ll.head

def main():
    ll = LinkedList()
    inp = [1, 2, 3, 4, 5]
    for e in inp:
        ll.add(e)
    ll.reorder()
    ll.print()

main()