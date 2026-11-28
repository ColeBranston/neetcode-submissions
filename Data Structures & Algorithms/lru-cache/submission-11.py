class Node():
    def __init__(self, val = 0, key = None, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node()
        self.right = Node()

        self.k = capacity

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self._delete(self.cache[key])
        self._insert(self.cache[key])
        
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            del self.cache[key]

            self._delete(node)

        self.cache[key] = Node(value, key)
        self._insert(self.cache[key])

        if len(self.cache) > self.k:
            if self.left.next.key in self.cache:
                del self.cache[self.left.next.key]
            self._delete(self.left.next)
        
    def _delete(self, node):
        prev = node.prev
        nextt = node.next

        prev.next = nextt
        nextt.prev = prev

    def _insert(self, node):
        second = self.right.prev
        
        self.right.prev = node
        second.next = node
        
        node.prev = second
        node.next = self.right






        

