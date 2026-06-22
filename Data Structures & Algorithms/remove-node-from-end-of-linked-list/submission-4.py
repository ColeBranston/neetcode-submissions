# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        ref = head
        while ref:
            N += 1
            ref = ref.next

        print("n:", n)
        print("N:", N)
        n = N - n

        print("n is now: ", n)

        ref = head
        counter = 0
        
        if n == 0:
            return ref.next
        while ref:
            if counter == n-1:
                print("skipping")
                ref.next = ref.next.next
                break

            counter +=1
            ref = ref.next

        return head