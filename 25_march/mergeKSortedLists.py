import heapq
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

def mergeKSortedLists(lls: list) -> LinkedList:
    if not lls:
        return None
    if len(lls) == 1:
        return lls[0]
    pq = []
    for ll in lls:
        it = ll.head
        while it:
            heapq.heappush(pq, it.val)
            it = it.next
    res = LinkedList()
    while pq:
        val = heapq.heappop(pq)
        res.add(val)
    return res

def main():
    lls = []
    n = int(input())
    for i in range(n):
        m = int(input())
        if not m:
            continue
        nums = map(int, input().split())
        ll = LinkedList()
        for elem in nums:
            ll.add(elem)
        lls.append(ll)
    mergedList = mergeKSortedLists(lls)
    if mergedList:
        mergedList.print()

main()