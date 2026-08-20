class Node:
    def __init__ (self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lNode = Node(0,0)
        self.rNode = Node(0,0)

        self.lNode.next = self.rNode
        self.rNode.prev = self.lNode

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        node = self.cache[key]
        self._del(node.key)
        self._insert(node.key, node.val)
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._del(key)
            
        self._insert(key, value)
        if len(self.cache) > self.cap:
            self._del(self.lNode.next.key)
        
    def _del(self, key):
        node = self.cache[key]
        print(node.key)
        l,r = node.prev, node.next
        l.next = r
        r.prev = l
        del self.cache[key]

    def _insert(self, key, val):
        latest = self.rNode.prev
        newNode = Node(key, val)

        newNode.prev = latest
        newNode.next = self.rNode

        self.cache[key] = newNode
        latest.next = newNode
        self.rNode.prev = newNode
