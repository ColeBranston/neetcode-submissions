class Node:
    def __init__ (self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    '''
        For this solution you use a cache and left and right pointer to add and remove nodes
        and form a doubly linked list, we make an additional 2 methods, delete and insert.
        Delete uses the prev and next pointers of the incoming node to delete the node in the linked list.
        Insert uses the right most pointer and connects the previous last node to the incoming node, and the prev
        pointer node to the prevous last node, then the incoming node to the lru right pointer and the lru right
        node's prev pointer to the incoming node.

        The get method simply checks the cache for the key, node pair, if the key is in the cache,
        the cached node is saved as a reference, deleted and then inserted once more to simulate its
        usage tracking.

        The insert method first checks if the key exists in the cache and deletes it otherwise the linked list
        and cache tracking would break. From there the node is re-cached by setting the key to the object: Node(key, val),
        next the node is then inserted into the linked list via the insert method. Lastly, the insert method, checks
        the max capacity with reference to the length of the cache, ie. if len(self.cache) > self.cap ... , if
        the cache has exceeded the capacity of the linked list, then the least used node is removed by taking the next
        pointer of the LRU's left node and deleting it from the linked list with the delete method, and removing
        the entry in the cache with del self.cache[least_used.key]
    '''

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
        if key in self.cache: # required otherwise you will mess up the cache and linked list
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        
