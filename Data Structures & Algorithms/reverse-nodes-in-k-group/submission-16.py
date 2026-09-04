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
                
            stop = kth.next
            prev = stop
            curr = start.next

            while curr != stop:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = start.next
            start.next = kth # this actually completes the reversal by ensuring that before the start is moved to the next node (previously unreversed, now reversed), that the kth node is wired in. Ex. on every first group for 1,2,3,4 k=3, dummy.next is 1 but then everything gets reversed and it becomes 3,2,1,4, now to ensure that everything continues, start.next ie. dummy.next on the first time is set to kth or 3, then start is set to 1 for the next itteration and it continues.
            # Further explanation is that on first time, start is ListNode(0 (dummy val), head (start of LL)), therefore making that reversal doesn't show in the dummy reference until its changed with start.next = kth node, so while the reversal does occur, the start.next still points to ListNode(1) and therefore would delete the reversed nodes if wasn't rewired with start.next = kth (now first node in the reversed LL)
            start = temp


        return dummy.next