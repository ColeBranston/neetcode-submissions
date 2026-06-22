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
        if not head:
            return None

        stor = {}

        ref = head
        while ref:
            stor[ref] = Node(ref.val)
            ref = ref.next

        ref = head
        while ref:
            stor[ref].next = stor.get(ref.next)
            stor[ref].random = stor.get(ref.random)
            ref = ref.next

        return stor[head]
