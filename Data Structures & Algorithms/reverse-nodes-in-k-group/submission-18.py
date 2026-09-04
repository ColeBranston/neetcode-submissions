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

        dummy = marker = ListNode(0, head)

        while True:
            kth = getKth(marker, k)
            if not kth:
                break

            stop = kth.next
            curr = marker.next
            prev = stop

            while curr != stop:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            markerTemp = marker.next
            marker.next = kth
            marker = markerTemp

        return dummy.next