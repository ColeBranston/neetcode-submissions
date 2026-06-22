class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ref -> head -> node1 -> node2 -> node3
        # prev = node3 -> node2 -> node1 -> head

        ref = head
        prev = None

        while ref:
            temp = ref.next
            ref.next = prev
            prev = ref
            ref = temp

        return prev