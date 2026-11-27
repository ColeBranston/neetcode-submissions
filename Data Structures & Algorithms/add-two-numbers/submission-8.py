# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumReverse(LL):
            ref = LL
            res = ""

            while ref:
                res += str(ref.val)
                ref = ref.next
            
            return res[::-1]

        l1 = int(getNumReverse(l1))
        l2 = int(getNumReverse(l2))

        combined = str(l1 + l2)[::-1]
        
        res = ref = ListNode()
        
        for num in [int(char) for char in combined]:
            ref.next = ListNode(num)
            ref = ref.next

        return res.next
