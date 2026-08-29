class LLNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = LLNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head
        curr_i = -1
        while curr:
            if curr_i == index:
                return curr.value
            curr = curr.next
            curr_i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LLNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        
    def insertTail(self, val: int) -> None:
        self.tail.next = LLNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and curr.next:
            if i == index:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return True
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res 
