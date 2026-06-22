class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref = head
        prev = None

        while ref:
            temp = ref.next
            ref.next = prev
            prev = ref
            ref = temp

        return prev