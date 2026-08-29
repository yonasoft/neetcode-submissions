class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = self.tail = Node(-1)

    def isEmpty(self) -> bool:
        return self.head.next == None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value, self.head.next)
        if self.isEmpty():
            self.tail = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.head
        while curr.next:
            if curr.next == self.tail:
                break
            curr = curr.next
        pop = self.tail.val
        curr.next = None
        self.tail = curr
        return pop
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        item = self.head.next
        self.head.next =  self.head.next.next
        return item.val
        
