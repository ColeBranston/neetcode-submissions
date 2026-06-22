class Node:
    def __init__ (self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def delete(self, node):
        # fills in the bridge between the prev and next pointers, deleting the node inbetween
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert (self, node):
        latest = self.right.prev
        latest.next, node.prev = node, latest
        node.next, self.right.prev = self.right, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.delete(node)
        self.insert(node)

        return node.val

    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        
