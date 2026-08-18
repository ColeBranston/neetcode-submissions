# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse = slow.next
        prev = slow.next = None

        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp

        dummyRef = dummy = ListNode()
        ref = head
        while prev:
            temp1,temp2 = ref.next,prev.next
            ref.next = prev
            prev.next = temp1
            ref,prev = temp1, temp2            