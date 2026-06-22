class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref = head
        rev = None 

        while ref:
            temp = ref.next
            ref.next = rev
            rev = ref
            ref = temp

        return rev