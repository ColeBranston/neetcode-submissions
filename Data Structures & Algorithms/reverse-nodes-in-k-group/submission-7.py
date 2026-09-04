# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        dummy = marker = ListNode(0, head)

        while True:
            kth = self.getKth(marker, k)
            if not kth:
                break

            groupNext = kth.next # the start of the next group
            prev = groupNext # start of the next group
            curr = marker.next # End of the previous group, but at first its the start of the linked list (head)
            while curr != groupNext: # reverses the group keeping the pointed to the groupNext
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = marker.next
            marker.next = kth
            marker = temp

        return dummy.next