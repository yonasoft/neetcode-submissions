class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [[] for i in range(self.capacity)]
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        index = self.getHash(key)
        for pair in self.arr[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.arr[index].append([key, value])
        self.size += 1
        if self.size >= self.capacity // 2:
            self.resize()


    def get(self, key: int) -> int:
        index = self.getHash(key)
        for pair in self.arr[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> bool:
        index = self.getHash(key)
        for i, pair in enumerate(self.arr[index]):
            if pair[0] == key:
                self.arr[index].pop(i)
                self.size -= 1
                return True
        return False
        

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity*=2
        new_arr = [[] for i in range(self.capacity)]
        for bucket in self.arr:
            for key,val in bucket:
                index = self.getHash(key)
                new_arr[index].append([key,val])
        self.arr = new_arr
    def getHash(self, key):
        return key % self.capacity

