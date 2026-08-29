class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root: 
            self.root = new_node
            return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                else:
                    curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                else:
                    curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def findMin(self, node) -> int:
        curr = node
        while node and node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.key)
            dfs(node.right)
        dfs(self.root)
        return res