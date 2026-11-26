"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two pass, with node cloning then hooking up
        cache = {}

        if not head:
            return None

        ref = head
        while ref:
            cache[ref] = Node(ref.val)
            ref = ref.next

        ref = head
        while ref:
            cache[ref].random = cache[ref.random] if ref.random else None     
            cache[ref].next = cache[ref.next] if ref.next else None

            ref = ref.next

        return cache[head]