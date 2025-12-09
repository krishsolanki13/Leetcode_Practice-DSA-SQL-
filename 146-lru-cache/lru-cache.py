class Node:
    def __init__(self, key:int, val:int):
        self.key, self.val = key, val
        self.next = self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right,self.left
    
    #Always insert to the right to maintain the cache
    def insert(self, node):
        next, prev = self.right, self.right.prev
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key:int, val:int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]