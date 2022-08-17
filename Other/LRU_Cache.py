class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to the node
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right #left = least recent
        self.right.prev = self.left #right = most recent

    def remove(self,node):
        if node.next and node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif not node.next and node.prev:
            node.prev.next = None
        else:
            node.next.prev = None
    
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            newLRU = self.left.next
            del self.cache[newLRU.key]
            self.remove(newLRU)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)