# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        stor = set()
        ref = head
        while ref:
            if ref.val in stor and ref.next:
                return True
            stor.add(ref.val)
            if not ref.next:
                break

            ref = ref.next
        return False