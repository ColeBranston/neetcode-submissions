# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        n = length - n
        ref = head
        counter = 0

        if n == 0:
            return ref.next

        while ref:
            if counter == n-1:
                ref.next = ref.next.next
                break

            counter += 1
            ref = ref.next

        return head