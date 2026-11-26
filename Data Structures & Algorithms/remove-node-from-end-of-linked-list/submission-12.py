# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ref = head

        counter = 0
        while ref:
            counter += 1
            ref = ref.next

        length = counter
        dist = length - n

        dummy = ref = head

        if dist == 0:
            return ref.next

        counter = 0
        trail = None
        while ref:
            if counter == dist:
                trail.next = ref.next
                break

            counter += 1
            trail = ref
            ref = ref.next
            

        return dummy