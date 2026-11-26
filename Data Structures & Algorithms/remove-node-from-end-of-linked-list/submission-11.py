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

        if length == 1:
            return None

        dummy = ref = head
        counter = 0
        trail = None
        while ref:
            if counter == dist:
                if trail:
                    trail.next = ref.next
                else:
                    return ref.next
                break

            counter += 1
            trail = ref
            ref = ref.next
            

        return dummy