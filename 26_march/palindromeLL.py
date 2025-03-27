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
    def isPalindrome(self):
        stk = []
        node = self.head
        count = 0
        while count < self.size // 2:
            stk.append(node.val)
            node = node.next
            count += 1
        if self.size & 1:
            node = node.next
        while node:
            if node.val != stk[-1]:
                return "false"
            else:
                node = node.next
                stk.pop()
        return "true"

def main():
    ll = LinkedList()
    n = input()
    inp = map(int, input().split())
    for e in inp:
        ll.add(e)
    print(ll.isPalindrome()) 

main()