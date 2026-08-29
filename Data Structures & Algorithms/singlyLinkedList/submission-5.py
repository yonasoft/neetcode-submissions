class LLNode:
    def __init__(self, val ):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr_i = 0
        curr = self.head
        while curr:
            if curr_i == index: 
                return curr.val
            curr_i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LLNode(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = LLNode(val)
        if not self.head: 
            self.head = new_node 
        else:
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            curr.next = new_node

    def remove(self, index: int) -> bool:
        prehead = LLNode(0)
        prehead.next = self.head 
        curr, curr_i = prehead, 0
        while curr and curr.next:
            if curr_i == index:
                curr.next = curr.next.next
                self.head = prehead.next
                return True
            curr_i += 1
            curr = curr.next
        return False
    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
