class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = self.tail = Node(-1)  # Dummy node as sentinel

    def isEmpty(self) -> bool:
        return self.head.next is None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head.next = new_node
            self.tail = new_node
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
        while curr.next != self.tail:
            curr = curr.next
        
        popped_value = self.tail.val
        if self.head.next == self.tail:  # If only one element exists
            self.head.next = None
            self.tail = self.head
        else:
            curr.next = None
            self.tail = curr
        
        return popped_value
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first_node = self.head.next
        self.head.next = first_node.next
        
        if first_node == self.tail:  # If it was the only node, reset tail
            self.tail = self.head
        
        return first_node.val
