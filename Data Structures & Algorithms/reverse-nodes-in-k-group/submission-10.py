# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k-=1
            return node

        dummy = start = ListNode(0,head)

        while True:
            kth = getKth(start, k)
            if not kth:
                break

            lastNode = kth.next
            prev = lastNode
            curr = start.next

            while curr != lastNode:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = start.next
            start.next = kth
            start = temp


        return dummy.next